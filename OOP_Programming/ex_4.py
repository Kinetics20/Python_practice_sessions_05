class Employee:
    def __init__(self, name, age, salary, position):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent / 100)

    def __str__(self):
        return (
            f"{self.name} is {self.age} years old,"
            f" and works as a {self.position}"
            f" with the salary of {self.salary}."
        )

    def __add__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return type(self)(self.name, self.age + other.age, self.position, self.salary)


    def __repr__(self):
        return f'{type(self).__name__}({', '.join(
            f'{key} = {val!r}'
            for key, val in vars(self).items())
        })'


e1 = Employee('John', 25,  'Software Engineer C1',10000)
e2 = Employee('Martyna', 35,  'Software Engineer C1',12000)

team = e1 + e2
print(team)
