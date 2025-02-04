# class Employee:
#     def __init__(self, name, age, salary, position):
#         self.name = name
#         self.age = age
#         self.salary = salary
#         self.position = position
#
#     def increase_salary(self, percent):
#         self.__dict__['salary'] += self.__dict__['salary'] * (percent / 100)
#
#     def info(self):
#         return (
#             f"{self.name} is {self.age} years old,"
#             f" and works as a {self.position}"
#             f" with the salary of {self.salary}."
#         )
#
# e = Employee('John', 25,10000, 'Software Engineer')
# print(e.__dict__)
#
# # Employee.increase_salary(e, 10)
# # print(e.__dict__)
#
# e.increase_salary(10)
# print(e.__dict__)
#
# print(e.info())

class Employee:
    def __init__(self, name, age, salary, position):
        self.name = name
        self.age = age
        self.salary = salary
        self.position = position

    def increase_salary(self, percent):
        self.salary += self.salary * (percent / 100)

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


e = Employee('John', 25,10000, 'Software Engineer')
print(e.__dict__)
print(vars(e))
# print(e)
# # print(str(e))
# print(repr(e))
