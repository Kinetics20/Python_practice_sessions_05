import pandas as pd
import pandera.pandas as pa
from pandera.typing import Series


raw_order_lines = pd.DataFrame(
    [
        {
            "batch_id": "BATCH-20260612-01",
            "event_id": "evt-0001",
            "order_id": "ORD-1001",
            "line_no": "1",
            "partner": "ACME_PL",
            "event_time": "2026-06-12 09:00:00",
            "sku": "BOOK-001",
            "quantity": "2",
            "unit_price": "19.99",
            "line_total": "39.98",
            "currency": "PLN",
            "country": "PL",
        },
        {
            "batch_id": "BATCH-20260612-01",
            "event_id": "evt-0001",
            "order_id": "ORD-1001",
            "line_no": "2",
            "partner": "ACME_PL",
            "event_time": "2026-06-12 09:00:00",
            "sku": "SHIP-STD",
            "quantity": "1",
            "unit_price": "5.50",
            "line_total": "5.50",
            "currency": "PLN",
            "country": "PL",
        },
        {
            "batch_id": "BATCH-20260612-01",
            "event_id": "evt-0002",
            "order_id": "ORD-1002",
            "line_no": "1",
            "partner": "ACME_DE",
            "event_time": "2026-06-12 09:03:00",
            "sku": "MUG-RED",
            "quantity": "3",
            "unit_price": "10.00",
            "line_total": "30.00",
            "currency": "EUR",
            "country": "DE",
        },
    ]
)

order_line_schema = pa.DataFrameSchema(
    columns={
        "batch_id": pa.Column(str, pa.Check.str_matches(r"^BATCH-\d{8}-\d{2}$")),
        "event_id": pa.Column(str, pa.Check.str_matches(r"^evt-\d{4}$")),
        "order_id": pa.Column(str, pa.Check.str_matches(r"^ORD-\d{4}$")),
        "line_no": pa.Column(int, pa.Check.ge(1)),
        "partner": pa.Column(str, pa.Check.str_matches(r"^[A-Z0-9_]{3,20}$")),
        "event_time": pa.Column(pa.DateTime),
        "sku": pa.Column(str, pa.Check.str_matches(r"^[A-Z0-9][A-Z0-9_-]+$")),
        "quantity": pa.Column(int, pa.Check.ge(1)),
        "unit_price": pa.Column(float, pa.Check.gt(0)),
        "line_total": pa.Column(float, pa.Check.gt(0)),
        "currency": pa.Column(str, pa.Check.isin(["PLN", "EUR", "USD"])),
        "country": pa.Column(str, pa.Check.isin(["PL", "DE", "CZ"])),
    },
    coerce=True,
    strict=True,
    name="OrderLineBach",
)

validate_order_lines = order_line_schema.validate(raw_order_lines)

# print(validate_order_lines)
# print('\nColumns types after Pandera')
# print(validate_order_lines.dtypes)

invalid_quantity = raw_order_lines.copy()

invalid_quantity.loc[0, 'quantity'] = '0'

# print(invalid_quantity[['order_id', 'line_no', 'quantity']])
#
# try:
#     order_line_schema.validate(invalid_quantity)
# except pa.errors.SchemaError as exc:
#     print(type(exc).__name__)
#     print(exc.failure_cases)

extra_columns = raw_order_lines.assign(debug_payload='temporary partner code')
# print(extra_columns.columns)
#
# try:
#     order_line_schema.validate(extra_columns)
# except pa.errors.SchemaError as exc:
#     print(type(exc).__name__)
#     print(exc.failure_cases)
# except pa.errors.SchemaErrors as exc:
#     print(type(exc).__name__)
#     print(exc.failure_cases)

filter_schema = pa.DataFrameSchema(
    columns = order_line_schema.columns,
    coerce=True,
    strict='filter',
    name='OrderLineBatchFilterMode'
)

# filtered = filter_schema.validate(extra_columns)
# print(filtered.columns)

wrong_order = raw_order_lines[
    [
        "order_id",
        *[column for column in raw_order_lines.columns if column != "order_id"],
    ]
]
# print(wrong_order.columns)

ordered_schema = pa.DataFrameSchema(
    order_line_schema.columns,
    coerce=True,
    strict=True,
    ordered=True,
    name="OrderLineBatchOrdered",
)
