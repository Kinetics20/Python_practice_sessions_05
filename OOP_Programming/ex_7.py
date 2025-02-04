class Employee:
    __slots__ = ('name', 'age', 'position', 'salary')

    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent / 100)

class Tester(Employee):
    def run_test(self):
        print(f'({self.name}) is testing...')
        print('All tests passed!')


class SlotsInspectorMixin:
    __slots__ = ()

    def has_slots(self):
        return hasattr(self, '__slots__')


class Developer(SlotsInspectorMixin, Employee):
    __slots__ = ('tech_stack',)

    def __init__(self, name, age, position, salary, tech_stack):
        super().__init__(name, age, position, salary)
        self.tech_stack = tech_stack

    def increase_salary(self, percent, bonus=0):
        super().increase_salary(percent)
        self.salary += bonus

e1 = Developer('John', 25,  'Software Engineer C1', 10000, 'python')
print(e1.has_slots())
print(Employee.__slots__)
# print(e1.__dict__)

# e1 = Tester('John', 25,  'Software Engineer C1', 10000)
# e2 = Developer('Kate', 35,  'Software Engineer C1', 12000, 'java')
#
# e1.increase_salary(20)
# e2.increase_salary(20, 50000)
# print(e2.tech_stack)

# print(e1.salary)
# print(e2.salary)

# print(isinstance(e1, Tester))
# print(isinstance(e1, Employee))
# print(isinstance(e1, object))

# print(issubclass(Developer, Employee))
# print(issubclass(Developer, object))
# print(issubclass(Employee, object))
# print(issubclass(Tester, Developer))
#
# try:
#     # raise FloatingPointError('Floating point error')
#     raise ZeroDivisionError('Division by zero')
# except ArithmeticError as e:
#     print(e)
