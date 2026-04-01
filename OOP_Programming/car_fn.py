def factory_car(brand, max_speed):
    return {
        'brand': brand,
        'engine': False,
        'speed': 0,
        'max_speed': max_speed
    }


def start_engine(car):
    if not car['engine']:
        car['engine'] = True
        print('You started the engine.')
    else:
        print('The engine is already started.')


def stop_engine(car):
    if car['speed'] == 0:
        car['engine'] = False
        print('You stopped the engine.')
    else:
        print('Stop the car at first.')


def speed_up(car, amount):
    if car['engine']:
        car['speed'] = min(car['speed'] + amount, car['max_speed'])
        print(f'You are driving with speed {car["speed"]}.')
    else:
        print('Start the engine at first.')


def slow_down(car, amount):
    car['speed'] = max(car['speed'] - amount, 0)
    print(f'You are driving with speed {car["speed"]}.')


auto = factory_car('BMW', 280)

start_engine(auto)
stop_engine(auto)
start_engine(auto)
speed_up(auto, 50)
speed_up(auto, 500)
stop_engine(auto)
slow_down(auto, 50)
slow_down(auto, 280)
stop_engine(auto)
