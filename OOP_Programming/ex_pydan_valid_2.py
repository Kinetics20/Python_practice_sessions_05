from __future__ import annotations
import json
from datetime import datetime, UTC
from pprint import pprint
from uuid import UUID, uuid4
from typing import Literal, Annotated, Any, Self
from decimal import Decimal, ROUND_HALF_UP
from pydantic import (
    BaseModel,
    Field,
    ConfigDict,
    AliasChoices,
    field_serializer,
    field_validator,
    computed_field,
    model_validator,
    TypeAdapter, ValidationError, validate_call, create_model,
)
from pydantic_settings import BaseSettings, SettingsConfigDict

Currency = Literal["PLN", "USD", "EUR"]
PartnerCode = Annotated[str, Field(pattern=r"^[A-Z0-9_]{3,20}$")]
Sku = Annotated[
    str, Field(min_length=3, max_length=40, pattern=r"^[A-Z0-9][A-Z0-9_-]+$")
]
Quantity = Annotated[int, Field(gt=0, le=999)]


class Customer(BaseModel):
    customer_id: Annotated[str, Field(pattern=r"^CUST-\d{4,}$")]
    loyalty_tier: Literal["standard", "gold", "vip"] = "standard"


class ShippingAddress(BaseModel):
    country: Literal["PL", "DE", "CZ"]
    city: Annotated[str, Field(min_length=2, max_length=80)]
    postal_code: Annotated[str, Field(pattern=r"^\d{2}-\d{3}$")]
    line1: Annotated[str, Field(min_length=5, max_length=120)]


class Money(BaseModel):
    amount: Decimal = Field(gt=0, max_digits=12, decimal_places=2)
    currency: Currency

    @field_serializer("amount", when_used="json")
    def serialize_amount(self, amount: Decimal) -> str:
        return format(amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP), "f")


class OrderItem(BaseModel):
    sku: Sku
    quantity: Quantity
    unit_price: Money

    @field_validator("sku", mode="before")
    @classmethod
    def normalize_sku(cls, value: Any) -> Any:
        if isinstance(value, str):
            return value.strip().upper().replace(" ", "_")
        return value

    @computed_field
    @property
    def line_total(self) -> Decimal:
        return (self.unit_price.amount * self.quantity).quantize(Decimal("0.01"))


class OrderTotals(BaseModel):
    items: list[OrderItem] = Field(min_length=1)
    declared_total: Money

    @model_validator(mode="after")
    def total_must_match_items(self) -> Self:
        currencies = {item.unit_price.currency for item in self.items} | {
            self.declared_total.currency
        }

        if len(currencies) != 1:
            raise ValueError(
                f"all order money values must share one currency, got {sorted(currencies)}"
            )

        computed = sum(
            (item.line_total for item in self.items), Decimal("0.00")
        ).quantize(Decimal("0.01"))
        declared = self.declared_total.amount.quantize(Decimal("0.01"))

        if computed != declared:
            raise ValueError(
                f"declared_total={declared} does not match computed_total={computed}"
            )

        return self


class CanonicalOrder(BaseModel):
    model_config = ConfigDict(extra="forbid")

    order_id: Annotated[str, Field(min_length=6, max_length=40)]
    partner: PartnerCode
    customer: Customer
    shipping: ShippingAddress
    totals: OrderTotals
    received_at: datetime = Field(default_factory=lambda: datetime.now(tz=UTC))


class EventEnvelope(BaseModel):
    model_config = ConfigDict(extra="forbid")

    event_id: UUID
    partner_code: Annotated[str, Field(pattern=r"^[A-Z0-9_]{3,20}$")]
    event_time: datetime


class OrderCreatedEvent(EventEnvelope):
    type: Literal["order.created"]
    order: CanonicalOrder


class OrderCancelledEvent(EventEnvelope):
    type: Literal["order.cancelled"]
    order_id: str
    reason: Annotated[str, Field(min_length=3, max_length=200)]


OrderEvent = Annotated[
    OrderCreatedEvent | OrderCancelledEvent, Field(discriminator="type")
]
OrderEventBatch = list[OrderEvent]

ORDER_EVENT_ADAPTER = TypeAdapter(OrderEvent)
ORDER_EVENT_BATCH_ADAPTER = TypeAdapter(OrderEventBatch)

data = {
    "order_id": "ORD-2026-0001",
    "partner": "MKP_EU",
    "customer": {"customer_id": "CUST-1001", "loyalty_tier": "gold"},
    "shipping": {
        "country": "PL",
        "city": "Warszawa",
        "postal_code": "00-001",
        "line1": "Prosta 1",
    },
    "totals": {
        "items": [
            {"sku": " sku-001 ", "quantity": "2", "unit_price": {"amount": "19.99", "currency": "PLN"}},
            {"sku": "sku 002", "quantity": 1, "unit_price": {"amount": Decimal("5.00"), "currency": "PLN"}},
        ],
        "declared_total": {"amount": "44.98", "currency": "PLN"},
    },
}

created = {
    "event_id": str(uuid4()),
    "type": "order.created",
    "partner_code": "MKP_EU",
    "event_time": "2026-06-08T09:15:00+00:00",
    "order": data,
}

cancelled = {
    "event_id": str(uuid4()),
    "type": "order.cancelled",
    "partner_code": "MKP_EU",
    "event_time": "2026-06-08T09:15:00+00:00",
    "order_id": 'customer John',
    'reason': 'customer request'
}

# events = ORDER_EVENT_BATCH_ADAPTER.validate_python([created, cancelled])
# print(events)
event_payload = dict(created)
payload_bytes = json.dumps(event_payload, default=str).encode('utf-8')
event = ORDER_EVENT_ADAPTER.validate_json(payload_bytes)

# print(event)
dumped = ORDER_EVENT_ADAPTER.dump_json(event)
# print(dumped)

schema = OrderCreatedEvent.model_json_schema()
# pprint(schema)