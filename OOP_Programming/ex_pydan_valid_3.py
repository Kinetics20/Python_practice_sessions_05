import json
from datetime import datetime, UTC
from decimal import Decimal
from typing import Literal, Annotated

from pydantic import BaseModel, EmailStr, Field, StringConstraints, ConfigDict, field_validator, computed_field, \
    field_serializer, ValidationError

CustomerId = Annotated[str, StringConstraints(pattern=r'^CUST-\d{5}$', strip_whitespace=True)]

EventId = Annotated[str, StringConstraints(pattern=r"^evt-\d{4}$", strip_whitespace=True)]

OrderId = Annotated[str, StringConstraints(pattern=r"^ORD-\d{4}$", strip_whitespace=True)]

PositiveDecimal = Annotated[Decimal, Field(gt=0)]

class CustomerSnapshot(BaseModel):
    """A minimal customer snapshot stored with the order event."""

    model_config = ConfigDict(
        title='Customer Snapshot',
        extra='forbid',
        validate_assignment=True,
        str_strip_whitespace=True,
        json_schema_extra={
            "summary": "Minimal customer data required to process an order event.",
            "examples": [
                {
                    "customer_id": "CUST-100001",
                    'email': 'a@example.com',
                    'segment': 'vip',
                }
            ]
        }
    )

    customer_id: CustomerId = Field(
        title="Customer identifier",
        description="A stable customer identifier in the marketplace system.",
        examples=["CUST-10001"],
        json_schema_extra={"summary": "Customer identifier in the CUST-12345 format."},
    )

    email: EmailStr = Field(
        title="Customer email",
        description="The email address captured when the order was accepted.",
        examples=["anna@example.com"],
        json_schema_extra={"summary": "A validated customer email address."},
    )

    segment: Literal["new", "regular", "vip"] = Field(
        default="new",
        title="Customer segment",
        description="Customer segment used by analytics and customer support.",
        examples=["regular"],
        json_schema_extra={"summary": "Allowed customer segment values."},
    )


class OrderCreatedEvent(BaseModel):
    """The order.created event validated as a single domain object."""

    model_config = ConfigDict(
        title="Order Created Event",
        extra="forbid",
        validate_assignment=True,
        validate_default=True,
        validate_by_alias=True,
        validate_by_name=True,
        str_strip_whitespace=True,
        json_schema_extra={
            "summary": "A domain event informing that a customer has placed an order.",
            "examples": [
                {
                    "eventId": "evt-0001",
                    "eventTime": "2026-06-12T09:00:00+00:00",
                    "order_id": "ORD-1001",
                    "customer": {
                        "customer_id": "CUST-10001",
                        "email": "anna@example.com",
                        "segment": "regular",
                    },
                    "items_count": 2,
                    "total_amount": "45.48",
                    "currency": "PLN",
                    "source": "web",
                }
            ],
        },
    )

    event_id: EventId = Field(
        alias="eventId",
        title="Event id",
        description="Identifier of the event received from the Order Intake Gateway.",
        examples=["evt-0001"],
        json_schema_extra={
            "summary": "The alias shows the difference between the Python field name and the JSON payload name."
        },
    )

    event_time: datetime = Field(
        alias="eventTime",
        title="Event time",
        description="The time when the event was generated.",
        examples=["2026-06-12T09:00:00+00:00"],
        json_schema_extra={
            "summary": "The datetime value is serialized by a field serializer."
        },
    )

    order_id: OrderId = Field(
        title="Order id",
        description="Order identifier.",
        examples=["ORD-1001"],
    )

    customer: CustomerSnapshot = Field(
        title="Customer snapshot",
        description="A nested Pydantic model containing customer data.",
    )

    items_count: int = Field(
        gt=0,
        title="Items count",
        description="Number of order items. Must be positive.",
        examples=[2],
    )

    total_amount: PositiveDecimal = Field(
        title="Total amount",
        description="Order amount stored as Decimal before serialization.",
        examples=["45.48"],
        json_schema_extra={
            "summary": "The Decimal value is validated numerically but serialized as a string with two decimal places."
        },
    )

    currency: Literal["PLN", "EUR", "USD"] = Field(
        title="Currency",
        description="Order currency.",
        examples=["PLN"],
    )

    source: Literal["web", "mobile", "partner_api"] = Field(
        default="web",
        title="Source",
        description="Order source channel.",
        examples=["web"],
    )

    @field_validator("currency", mode="before")
    @classmethod
    def normalize_currency(cls, value: object) -> object:

        if isinstance(value, str):
            return value.strip().upper()

        return value

    @field_validator("order_id")
    @classmethod
    def reject_placeholder_order_id(cls, value: str) -> str:

        if value == "ORD-0000":
            raise ValueError("ORD-0000 is a placeholder, not a real order")

        return value

    @computed_field(return_type=str)
    @property
    def summary(self) -> str:

        return (
            f"{self.order_id}: "
            f"{self.items_count} items / "
            f"{self.total_amount:.2f} {self.currency}"
        )

    @field_serializer("event_time", when_used="json")
    def serialize_event_time(self, value: datetime) -> str:

        return value.astimezone(UTC).isoformat().replace("+00:00", "Z")

    @field_serializer("total_amount", when_used="json")
    def serialize_total_amount(self, value: Decimal) -> str:

        return f"{value:.2f}"

    @field_validator("currency", mode="before")
    @classmethod
    def normalize_currency(cls, value: object) -> object:

        if isinstance(value, str):
            return value.strip().upper()

        return value

    @field_validator("order_id")
    @classmethod
    def reject_placeholder_order_id(cls, value: str) -> str:

        if value == "ORD-0000":
            raise ValueError("ORD-0000 is a placeholder, not a real order")

        return value

    @computed_field(return_type=str)
    @property
    def summary(self) -> str:

        return (
            f"{self.order_id}: "
            f"{self.items_count} items / "
            f"{self.total_amount:.2f} {self.currency}"
        )

    @field_serializer("event_time", when_used="json")
    def serialize_event_time(self, value: datetime) -> str:

        return value.astimezone(UTC).isoformat().replace("+00:00", "Z")

    @field_serializer("total_amount", when_used="json")
    def serialize_total_amount(self, value: Decimal) -> str:

        return f"{value:.2f}"


sth = CustomerSnapshot(customer_id='cl-001', email='a@a.com', segment='vip')
cn = CustomerSnapshot.model_validate({'customer_id': 'CUST-0001', 'email': 'a@a.com', 'segment': 'vip'})

print(cn.customer_id)

pydantic_payload = {
    "eventId": "evt-0001",
    "eventTime": "2026-06-12T09:00:00+02:00",
    "order_id": "ORD-1001",
    "customer": {
        "customer_id": " CUST-10001 ",
        "email": " anna@example.com ",
        "segment": "regular",
    },
    "items_count": 2,
    "total_amount": "45.48",
    "currency": " pln ",
    "source": "web",
}

event = OrderCreatedEvent.model_validate(pydantic_payload)
print("\nValidated object:")
print(event)

print("\nComputed summary:")

print(event.summary)

print("\nmodel_dump, Python dict:")

print(event.model_dump())

print("\nmodel_dump(mode='json', by_alias=True), API/JSON-ready version:")

print(event.model_dump(mode="json", by_alias=True))

print("\nmodel_dump_json with serializers:")

print(event.model_dump_json(by_alias=True, indent=2))

print("\nJSON Schema fragment: summary and examples:")

pydantic_schema = OrderCreatedEvent.model_json_schema()

print("schema summary:", pydantic_schema["summary"])

print("schema example:", pydantic_schema["examples"][0])

print("field summary:", pydantic_schema["properties"]["eventId"]["summary"])

print("field examples:", pydantic_schema["properties"]["eventId"]["examples"])

print("\nAssignment validation thanks to validate_assignment=True:")

try:
    event.items_count = 0

except ValidationError as exc:
    print(exc.errors(include_url=False))

print("\nSeveral errors at once:")

bad_payload = {
    **pydantic_payload,
    "eventId": "debug-1",
    "order_id": "ORD-0000",
    "currency": "gbp",
    "unexpected_field": "I should not be here",
    "customer": {
        **pydantic_payload["customer"],
        "segment": "gold",
        "unexpected_customer_field": "also invalid",
    },
}

try:
    OrderCreatedEvent.model_validate(bad_payload)

except ValidationError as exc:
    print(json.dumps(exc.errors(include_url=False, include_context=False), indent=2))