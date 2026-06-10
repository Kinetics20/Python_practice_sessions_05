from datetime import datetime, UTC
from decimal import Decimal
from typing import Literal, Annotated
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, ConfigDict, AliasChoices

Currency = Literal['PLN', 'USD', 'EUR']
PartnerCode = Annotated[str, Field(pattern=r'^[A-Z0-9_]{3,20}$')]


class IngressMoney(BaseModel):
    amount: Decimal = Field(gt=0, max_digits=12, decimal_places=2)
    currency: Currency


# m = IngressMoney(amount='12.50', currency='PLN')
# print(m.amount, m.currency)

class StrictEnvelope(BaseModel):
    model_config = ConfigDict(strict=True, extra='forbid')

    event_id: UUID
    version: Literal[1]
    partner_code: Annotated[str, Field(pattern=r'^[A-Z0-9_]{3,20}$')]
    event_time: datetime


StrictEnvelope(
    event_id=uuid4(),
    version=1,
    partner_code='TEC_8999',
    event_time=datetime.now(tz=UTC),
)


class PartnerOrder(BaseModel):
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    order_id: str = Field(
        validation_alias=AliasChoices('orderId', 'order_id', 'id'),
        serialization_alias='orderId'
    )
    partner_code: PartnerCode = Field(validation_alias=AliasChoices('merchant', 'partner'))


ref = PartnerOrder.model_validate({'id': 'EXT-42', 'merchant': 'ZSC_2005'})

print(ref.order_id, ref.partner_code)
print(ref.model_dump(by_alias=True))
print(ref.model_dump_json(by_alias=True))


# models' composition

class Customer(BaseModel):
    customer_id: Annotated[str, Field(pattern=r'^CUST-\d{4,}$')]
    loyalty_tier: Literal['standard', 'gold', 'vip'] = 'standard'


class ShippingAddress(BaseModel):
    country: Literal["PL", "DE", "CZ"]
    city: Annotated[str, Field(min_length=2, max_length=80)]
    postal_code: Annotated[str, Field(pattern=r"^\d{2}-\d{3}$")]
    line1: Annotated[str, Field(min_length=5, max_length=120)]


class CanonicalOrder(BaseModel):
    model_config = ConfigDict(extra='forbid')

    order_id: Annotated[str, Field(min_length=6, max_length=40)]
    partner: PartnerCode
    customer: Customer
    shipping: ShippingAddress
