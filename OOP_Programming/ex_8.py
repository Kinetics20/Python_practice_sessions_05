class Employee:
    max_salary = 10000

    def __init__(self, salary):
        self.salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value > type(self).max_salary:
            raise ValueError('Salary cannot be greater than 10000')
        self._salary = value


    def adjust_max_salary(self, value):
        type(self).max_salary = value

class Tester(Employee):
    pass

e = Tester(10000)
e2 = Employee(5555)

# e.adjust_max_salary(30000)
# print(e.max_salary)
# print(Employee.max_salary)
# print(Tester.max_salary)
# print(e2.max_salary)


# Employee.max_salary = 20000
# e = Employee(10000)
# e.max_salary = 8888
# e.adjust_max_salary(99)
# print(Employee.max_salary)

class X:

    __hash__ = None

x = X()
print(hash(x))