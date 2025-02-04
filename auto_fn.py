# simulation car working
# car brand, speed, max_speed, engine
# start_engine, stop_engine, speed_up, slow_down


def construct_auto(brand, max_speed):
    return {
    'brand:': brand,
    'speed': 0,
    'max_speed': max_speed,
    'engine': False
    }


bmw = construct_auto('E46', 180)
fiat = construct_auto('Uno', 240)

# bmw = {
#     'brand:': 'E46',
#     'speed': 0,
#     'max_speed': 180,
#     'engine': False
# }

# fiat = {
#     'brand:': 'uno',
#     'speed': 0,
#     'max_speed': 240,
#     'engine': False
# }

def start_engine(car):
    if not car['engine']:
        car['engine'] = True
        print('You started the engine')
    else:
        print('The engine was already launched')


def stop_engine(car):
    if car['speed'] == 0:
        car['engine'] = False
        print('You stopped the engine')
    else:
        print('Stop the car at first')


def speed_up(car, amount):
    if car['engine']:
        # if car['speed'] + amount > car['max_speed']:
        #     car['speed'] = car['max_speed']
        car['speed'] = min(car['speed'] + amount, car['max_speed'])
        # else:
            # car['speed'] += amount
        print(f'You are driving with speed {car["speed"]}')
    else:
        print('Start the engine at first')


def slow_down(car, amount):
    car['speed'] = max(car['speed'] - amount, 0)
    print(f'you are driving with speed {car["speed"]}')


# speed_up(bmw, amount=50)
start_engine(bmw)
speed_up(bmw, amount=50)
speed_up(bmw, amount=50)
speed_up(bmw, amount=50)
speed_up(bmw, amount=50)
# stop_engine(bmw)
slow_down(bmw, amount=50)
slow_down(bmw, amount=506666666)
stop_engine(bmw)
