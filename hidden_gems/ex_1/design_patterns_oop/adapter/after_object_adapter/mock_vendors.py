from hidden_gems.ex_1.design_patterns_oop.adapter.after_object_adapter.vendor import Vendor
from hidden_gems.ex_1.design_patterns_oop.adapter.after_object_adapter.vendor_adapter import VendorAdapter

MOCKCVENDORS = (
    VendorAdapter(Vendor('Pizza Love', '33', 'Pepperoni Lane')),
    VendorAdapter(Vendor('Happy and Green', '25', 'Kale St.')),
    VendorAdapter(Vendor('Sweet Tooth', '42', 'Chocolate Ave.'))
)