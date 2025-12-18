from hidden_gems.ex_1.design_patterns_oop.adapter.after_object_adapter.mock_customers import MOCKCUSTOMERS
from hidden_gems.ex_1.design_patterns_oop.adapter.after_object_adapter.mock_vendors import MOCKCVENDORS

MOCK = MOCKCVENDORS + MOCKCUSTOMERS

def main():
    for item in MOCK:
        print(f'Name {item.name}, Address {item.address}')

if __name__ == '__main__':
    main()
