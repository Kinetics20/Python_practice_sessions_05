class Programmer:
    def __init__(self, value):
        # if value < 0:
        #     raise ValueError(f'Age is too low: {value}')

        self.experience = value

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, new_value):
        if new_value < 0:
            raise ValueError(f'Age is too low: {new_value}')

        self._experience = new_value


    # experience = property(get_experience, set_experience)

    # @property
    # def expereience2(self):
    #     return f'{self._expereience2} yers'
    #
    # @expereience2.setter
    # def expereience2(self, value):
    #     if value < 0:
    #         raise ValueError(f'Age is too low{value}')
    #     self._expereience2 = value


    def __str__(self):
        if self._experience <= 5:
            title = 'junior'
        elif self._experience <= 10:
            title = 'regular'
        else:
            title = 'senior'
        return f'{self._experience} - {title}'




junior = Programmer(3)
# print(dir(junior))
print(vars(junior))
# junior.set_experience(12)
junior.experience = 10
# # junior._experience = -7777
# print(junior.get_experience())
print(junior.experience)
print(junior)

