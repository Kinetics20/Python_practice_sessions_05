class Employee:
    max_salary = 10000

    def __init__(self, salary):
        self.salary = salary + self.max_salary

e = Employee(10000)
print(e.salary)