class Car:
    def __init__(self, brand, max_speed):
        self.brand = brand
        self.speed = 0
        self.max_speed = max_speed
        self.engine = False

    def start_engine(self):
        if not self.engine:
            self.engine = True
            print('You started the engine')
        else:
            print('The engine was already launched')

    def stop_engine(self):
        if self.speed == 0:
            self.engine = False
            print('You stopped the engine')
        else:
            print('Stop the car at first')

    def speed_up(self, amount):
        if self.engine:
            self.speed = min(self.speed + amount, self.max_speed)
            print(f'You are driving with speed {self.speed}')
        else:
            print('Start the engine at first')

    def slow_down(self, amount):
        self.speed = max(self.speed - amount, 0)
        print(f'you are driving with speed {self.speed}')


bmw = Car('E46', 180)
fiat = Car('Uno', 240)
citroen = Car('c3', 175)

citroen.start_engine()
Car.speed_up(citroen, 100) # wywolanie metody za pomoca class-y / nie uzywamy /
# syntactic sugar
citroen.speed_up(60)
citroen.speed_up(60)
citroen.speed_up(60)
citroen.speed_up(60)
citroen.slow_down(20)
citroen.slow_down(200)
citroen.stop_engine()
