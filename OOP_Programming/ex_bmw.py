from __future__ import annotations

from abc import ABC, abstractmethod
from typing import override


class Engine:
    def __init__(self, power: int, fuel_type: str) -> None:
        self.power: int = power
        self._fuel_type: str = fuel_type

    @property
    def power(self) -> int:
        return self._power

    @power.setter
    def power(self, value: int) -> None:
        if value <= 60:
            raise ValueError('Engine power must be greater than 60 kW.')
        self._power = value

    @property
    def fuel_type(self) -> str:
        return self._fuel_type

    def start(self) -> str:
        return 'Engine started'


class ElectricEngine(Engine):
    def __init__(self, power: int, battery_level: int) -> None:
        super().__init__(power, fuel_type='electric')
        self.battery_level = battery_level

    @property
    def battery_level(self) -> int:
        return self._battery_level

    @battery_level.setter
    def battery_level(self, value: int) -> None:
        if value < 0 or value > 100:
            raise ValueError('Battery should not be less than zero and grater than 100.')
        self._battery_level = value

    @override
    def start(self) -> str:
        if self.battery_level <= 15:
            raise ValueError('Battery level should be greater than 15 percent.')
        return 'Electric engine started.'


class Vehicle(ABC):
    def __init__(self, brand: str, model: str, year: int, mileage: int) -> None:
        self._brand: str = brand
        self._model: str = model
        self._year: int = year
        self.mileage: int = mileage

    @property
    def brand(self) -> str:
        return self._brand

    @property
    def model(self) -> str:
        return self._model

    @property
    def year(self) -> int:
        return self._year

    @property
    def mileage(self) -> int:
        return self._mileage

    @mileage.setter
    def mileage(self, value: int) -> None:
        if value < 0:
            raise ValueError('Mileage cannot be negative.')
        self._mileage = value

    @abstractmethod
    def start_engine(self) -> str:
        ...

    def stop_engine(self) -> str:
        return 'Engine stopped'

    def vehicle_info(self) -> str:
        return f'Brand: {self.brand}, model: {self.model}, year: {self.year}, mileage: {self.mileage}'


class Car(Vehicle):
    def __init__(self, brand: str, model: str, year: int, mileage: int, doors: int, engine: Engine) -> None:
        super().__init__(brand, model, year, mileage)
        self.doors: int = doors
        self._engine: Engine = engine

    @property
    def doors(self) -> int:
        return self._doors

    @doors.setter
    def doors(self, value: int) -> None:
        if value < 3:
            raise ValueError('Amount of doors should be at least 3.')
        self._doors = value

    @property
    def engine(self) -> Engine:
        return self._engine

    def drive(self, km: int) -> None:
        if km <= 0:
            raise ValueError('Distance must be greater than zero.')
        self.mileage += km

    @abstractmethod
    def open_trunk(self) -> str:
        ...


class BMW(Car):
    def __init__(
            self,
            model: str,
            year: int,
            mileage: int,
            doors: int,
            engine: Engine,
            series: str,
            has_xdrive: bool

    ) -> None:
        super().__init__(brand='BMW', model=model, year=year, mileage=mileage, doors=doors, engine=engine)

        self.series = series
        self._has_xdrive: bool = has_xdrive

    @property
    def series(self) -> str:
        return self._series

    @series.setter
    def series(self, value: str) -> None:
        if value.strip() not in ('1', '2', '3', '4', '5', '6', '7', 'X1', 'X2', 'X3', 'X5', 'X6'):
            raise ValueError('Entered series does not exist.')
        self._series = value.strip()

    @property
    def has_xdrive(self) -> bool:
        return self._has_xdrive

    @override
    def start_engine(self) -> str:
        return self.engine.start()

    @override
    def open_trunk(self) -> str:
        return f'The trunk of the {self.brand} {self.model} now is open.'

    def activate_sport_mode(self) -> str:
        return 'The sport mode is active.'

