from hidden_gems.ex_1.design_patterns_oop.adapter.after_object_adapter.cust_adapter import CustAdapter
from hidden_gems.ex_1.design_patterns_oop.adapter.after_object_adapter.customer import Customer

MOCKCUSTOMERS = (
    CustAdapter(Customer('Pizza Love', '33 Pepperoni Lane')),
    CustAdapter(Customer('Happy and Green', '25 Kale St.')),
    CustAdapter(Customer('Sweet Tooth', '42 Chocolate Ave.'))
)
