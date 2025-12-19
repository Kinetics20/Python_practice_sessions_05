from hidden_gems.ex_1.design_patterns_oop.decorator.after.cars.luxury import Luxury
from hidden_gems.ex_1.design_patterns_oop.decorator.after.decorators.black import Black
from hidden_gems.ex_1.design_patterns_oop.decorator.after.decorators.leather import V6
from hidden_gems.ex_1.design_patterns_oop.decorator.after.decorators.vinyl import Vinyl


def show_car(car):
    print(f'Description: {car.description}, cost: {car.cost}')


def main():
    car = Luxury()
    show_car(car)
    car = V6(car)
    show_car(car)
    car = Vinyl(car)
    show_car(car)
    car = Black(car)
    show_car(car)

if __name__ == '__main__':
    main()