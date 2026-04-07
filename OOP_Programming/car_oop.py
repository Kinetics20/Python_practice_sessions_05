class Auto:
    def __init__(self, brand, max_speed):
        self.brand = brand
        self.engine = False
        self.speed = 0
        self.max_speed = max_speed

    def start_engine(self):
        if not self.engine:
            self.engine = True
            print('You started the engine.')
        else:
            print('The engine is already started.')

    def stop_engine(self):
        if self.speed == 0:
            self.engine = False
            print('You stopped the engine.')
        else:
            print('Stop the car at first.')

    def speed_up(self, amount):
        if self.engine:
            self.speed = min(self.speed + amount, self.max_speed)
            print(f'You are driving with speed {self.speed}.')
        else:
            print('Start the engine at first.')

    def slow_down(self, amount):
        self.speed = max(self.speed - amount, 0)
        print(f'You are driving with speed {self.speed}.')

    def __str__(self):
        return f"Brand: {self.brand}, Engine: {self.engine}, Speed: {self.speed}, Max_speed: {self.max_speed} km/h"

auto = Auto('BMW', 200)

auto.start_engine()
auto.stop_engine()
auto.start_engine()
auto.speed_up(50)
auto.speed_up(500)
auto.stop_engine()
auto.slow_down(50)
auto.slow_down(280)
auto.stop_engine()
print(auto)