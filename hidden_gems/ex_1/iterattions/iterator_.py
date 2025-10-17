class Car:
    def __init__(self, cars):
        self._cars = cars
        self._idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._idx >= len(self._cars):
            raise StopIteration

        result = self._cars[self._idx]
        self._idx += 1
        return result





# for car in Car(['BMW', 'Fiat', 'Dodge']):
#     print(car)

cars = Car(['BMW', 'Fiat', 'Dodge'])

# print(next(cars))

continents = {
    'africa': {
        'egypt': 'cairo',
        'libya': 'tripoli',
        'nigeria': 'abuja',
        'kenya': 'nairobi',
        'south_africa': 'pretoria',
        'morocco': 'rabat',
        'ethiopia': 'addis ababa',
        'ghana': 'accra'
    },
    'europe': {
        'germany': 'berlin',
        'poland': 'warsaw',
        'france': 'paris',
        'italy': 'rome',
        'spain': 'madrid',
        'netherlands': 'amsterdam',
        'sweden': 'stockholm',
        'norway': 'oslo',
        'finland': 'helsinki',
        'ukraine': 'kyiv'
    },
    'asia': {
        'china': 'beijing',
        'japan': 'tokyo',
        'india': 'new delhi',
        'south_korea': 'seoul',
        'thailand': 'bangkok',
        'vietnam': 'hanoi',
        'indonesia': 'jakarta',
        'saudi_arabia': 'riyadh'
    },
    'north_america': {
        'usa': 'washington d.c.',
        'canada': 'ottawa',
        'mexico': 'mexico city',
        'cuba': 'havana',
        'panama': 'panama city',
        'guatemala': 'guatemala city'
    },
    'south_america': {
        'brazil': 'brasilia',
        'argentina': 'buenos aires',
        'chile': 'santiago',
        'peru': 'lima',
        'colombia': 'bogota',
        'venezuela': 'caracas'
    },
    'australia': {
        'australia': 'canberra',
        'new_zealand': 'wellington',
        'fiji': 'suva',
        'papua_new_guinea': 'port moresby'
    }
}


class CapitalsIterator:
    def __init__(self, capitals):
        self._capitals = capitals
        self._idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._idx >= len(self._capitals):
            raise StopIteration

        capital = self._capitals[self._idx]
        self._idx += 1
        return capital


class Capitals:
    def __init__(self, continents_):
        self._continents = continents_

    def __iter__(self):
        capitals = []
        for countries in self._continents.values():
            capitals.extend(countries.values())

        capitals.sort()
        return CapitalsIterator(capitals)

capitals = Capitals(continents)

for capital in capitals:
    print(capital)