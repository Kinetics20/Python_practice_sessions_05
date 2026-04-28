from abc import ABC, abstractmethod
from typing import override


class Processor:
    def __init__(
            self,
            name: str,
            cores: int,
            base_clock_ghz: float
    ) -> None:
        self._name: str = name
        self.cores: int = cores
        self.base_clock_ghz: float = base_clock_ghz

    @property
    def name(self) -> str:
        return self._name

    @property
    def cores(self) -> int:
        return self._cores

    @cores.setter
    def cores(self, value: int) -> None:
        if value < 2:
            raise ValueError('Number of cores should be 2 or greater.')
        self._cores = value

    @property
    def base_clock_ghz(self) -> float:
        return self._base_clock_ghz

    @base_clock_ghz.setter
    def base_clock_ghz(self, value: float) -> None:
        if value < 2.0:
            raise ValueError('Base clock should be at least 2.0 GHz')
        self._base_clock_ghz = value

    def boost(self) -> str:
        return 'Boost mode is enabled'


class Battery:
    def __init__(self, capacity_mah: int, charge_level: int) -> None:
        self.capacity_mah: int = capacity_mah
        self.charge_level: int = charge_level

    @property
    def capacity_mah(self) -> int:
        return self._capacity_mah

    @capacity_mah.setter
    def capacity_mah(self, value: int) -> None:
        if value < 1000:
            raise ValueError('Battery capacity should be at least 1000 mAh.')
        self._capacity_mah = value

    @property
    def charge_level(self) -> int:
        return self._charge_level

    @charge_level.setter
    def charge_level(self, value: int) -> None:
        if not 0 <= value <= 100:
            raise ValueError('Charge level should be in range from 0 to 100.')
        self._charge_level = value

    def charge(self) -> str:
        return 'Battery is charging.'


class Device(ABC):
    def __init__(self, brand: str, model: str, year: int, serial_number: str) -> None:
        self._brand: str = brand
        self._model: str = model
        self._year: int = year
        self._serial_number: str = serial_number

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
    def serial_number(self) -> str:
        return self._serial_number

    @abstractmethod
    def power_on(self) -> str:
        ...

    def power_off(self) -> str:
        return 'The device is turned off.'

    def device_info(self) -> str:
        return f'Brand: {self.brand}, model: {self.model}, year: {self.year}, serial_number: {self.serial_number}'


class Computer(Device):
    def __init__(
            self,
            brand: str,
            model: str,
            year: int,
            serial_number: str,
            ram_gb: int,
            storage_gb: int,
            processor: Processor
    ) -> None:
        super().__init__(brand, model, year, serial_number)
        self.ram_gb: int = ram_gb
        self.storage_gb: int = storage_gb
        self._processor: Processor = processor

    @property
    def ram_gb(self) -> int:
        return self._ram_gb

    @ram_gb.setter
    def ram_gb(self, value: int) -> None:
        if value < 8:
            raise ValueError('RAM should be at least 8 GB.')
        self._ram_gb = value

    @property
    def storage_gb(self) -> int:
        return self._storage_gb

    @storage_gb.setter
    def storage_gb(self, value: int) -> None:
        if value < 500:
            raise ValueError('Storage must be at least 500 GB.')
        self._storage_gb = value

    @property
    def processor(self) -> Processor:
        return self._processor

    def run_program(self, program_name: str) -> str:
        return f'{program_name} is now running.'

    def upgrade_ram(self, extra_gb: int) -> None:
        if extra_gb <= 0 or extra_gb % 2 != 0:
            raise ValueError('Extra RAM should be greater than 0 and an even number.')
        self.ram_gb += extra_gb

    @abstractmethod
    def open_lid(self) -> str:
        ...


class Laptop(Computer):
    def __init__(
            self,
            brand: str,
            model: str,
            year: int,
            serial_number: str,
            ram_gb: int,
            storage_gb: int,
            processor: Processor,
            battery: Battery,
            screen_size: float
    ) -> None:
        super().__init__(brand, model, year, serial_number, ram_gb, storage_gb, processor)
        self._battery: Battery = battery
        self.screen_size: float = screen_size

    @property
    def battery(self) -> Battery:
        return self._battery

    @property
    def screen_size(self) -> float:
        return self._screen_size

    @screen_size.setter
    def screen_size(self, value: float) -> None:
        if value < 10:
            raise ValueError('Screen size must be at least 10 inches.')
        self._screen_size = value

    @override
    def power_on(self) -> str:
        return f'Laptop {self.brand} {self.model} is running.'

    @override
    def open_lid(self) -> str:
        return "The laptop's lid is open."

    def sleep_mode(self) -> str:
        return 'Laptop is now in sleep mode.'


class GamingLaptop(Laptop):
    def __init__(
            self,
            brand: str,
            model: str,
            year: int,
            serial_number: str,
            ram_gb: int,
            storage_gb: int,
            processor: Processor,
            battery: Battery,
            screen_size: float,
            gpu_model: str,
            rgb_keyboard: bool
    ) -> None:
        super().__init__(brand, model, year, serial_number, ram_gb, storage_gb, processor, battery, screen_size)
        self.gpu_model: str = gpu_model
        self._rgb_keyboard: bool = rgb_keyboard

    @property
    def gpu_model(self) -> str:
        return self._gpu_model

    @gpu_model.setter
    def gpu_model(self, value: str) -> None:
        if not value.strip().startswith('RTX'):
            raise ValueError('Gaming laptop should have an RTX graphics card.')
        self._gpu_model = value.strip()

    @property
    def rgb_keyboard(self) -> bool:
        return self._rgb_keyboard

    @override
    def power_on(self) -> str:
        return f"Gaming laptop {self.brand} {self.model} is ready for high-performance gaming."

    def enable_turbo_mode(self) -> str:
        return f'{self.brand}, {self.model} is now in turbo mode.'


