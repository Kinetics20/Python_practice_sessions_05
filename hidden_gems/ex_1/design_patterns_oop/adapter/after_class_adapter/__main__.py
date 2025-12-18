from hidden_gems.ex_1.design_patterns_oop.adapter.after_class_adapter.customer import Customer
from hidden_gems.ex_1.design_patterns_oop.adapter.after_class_adapter.mock_customers import MOCKCUSTOMERS
from hidden_gems.ex_1.design_patterns_oop.adapter.after_class_adapter.mock_vendors import MOCKCVENDORS

MOCK = MOCKCVENDORS + MOCKCUSTOMERS

def main():
    for item in MOCK:
        if isinstance(item, Customer):
            print(f'Name {item.name}, Address {item.address}')

if __name__ == '__main__':
    main()
