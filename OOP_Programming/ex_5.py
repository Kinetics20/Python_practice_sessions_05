class Employee:
    def __init__(self, name, age, salary, position):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent / 100)

    @property
    def salary_gross(self):
        return self._salary * 1.2

    @property
    def salary(self):
        print('Getting salary')
        return self._salary

    @salary.setter
    def salary(self, salary):
        print('Setting salary')
        if salary < 10000:
            raise ValueError("Salary must be greater than 10000")
        self._salary = salary

    @salary.deleter
    def salary(self):
        del self._salary



    def __str__(self):
        return (
            f"{self.name} is {self.age} years old,"
            f" and works as a {self.position}"
            f" with the salary of {self.salary}."
        )

    def __repr__(self):
        return f'{type(self).__name__}({', '.join(
            f'{key} = {val!r}'
            for key, val in vars(self).items())
        })'


e1 = Employee('John', 25, 10000, 'Software Engineer C1')
# print(e1.salary)
# print(e1.salary_gross)

# e1._salary = 4.0
# e1.set_salary(10001)
# print(e1.get_salary())
# e1.salary = 3.50
# e2 = Employee('Martyna', 35, 'Software Engineer C1', 12000)

# print(e1)
print(vars(e1))
print(vars(Employee))
