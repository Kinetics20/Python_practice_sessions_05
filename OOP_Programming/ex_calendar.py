from __future__ import annotations
from datetime import datetime, timedelta
from abc import ABC, abstractmethod
from typing import override


class Event(ABC):
    def __init__(self, title: str, start: datetime, duration_minutes: int, location: str = ''):
        self.title: str = title
        self._start: datetime = start
        self.duration_minutes: int = duration_minutes
        self._location: str = location

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value) -> None:
        if not value.strip():
            raise ValueError(f'Title cannot be empty string.')

        self._title = value

    @property
    def start(self) -> datetime:
        return self._start

    @property
    def duration_minutes(self) -> int:
        return self._duration_minutes

    @duration_minutes.setter
    def duration_minutes(self, value) -> None:
        if value <= 0:
            raise ValueError('The duration_minutes cannot be less or equal zero.')
        self._duration_minutes = value

    @property
    def location(self) -> str:
        return self._location

    @property
    def end(self) -> datetime:
        return self.start + timedelta(minutes=self.duration_minutes)

    def overlap_with(self, other: Event) -> bool:
        return self.start < other.end and other.start < self.end

    @abstractmethod
    def describe(self) -> str:
        ...

    @staticmethod
    @abstractmethod
    def category():
        ...

    def __str__(self):
        return f'{self.start:%H:%M} - {self.end:%H:%M} | {self.title}'


class Workshop(Event):
    def __init__(
            self,
            title: str,
            start: datetime,
            duration_minutes: int,
            instructor: str,
            capacity: int,
            location: str = ''
    ) -> None:
        super().__init__(title, start, duration_minutes, location)
        self.instructor = instructor
        self.capacity = capacity
        self._participants: list[str] = []

    @property
    def capacity(self) -> int:
        return self._capacity

    @capacity.setter
    def capacity(self, value) -> None:
        if value <= 0:
            raise ValueError(f'Capacity must be > 0')
        self._capacity = value

    def register(self, name: str) -> None:
        if len(self._participants) >= self._capacity:
            raise ValueError('Workshop is full')

        self._participants.append(name)

    @override
    @staticmethod
    def category() -> str:
        return 'Workshop'

    @override
    def describe(self) -> str:
        return (
            f'Workshop: {self.title}\n'
            f'Instructor: {self.instructor}\n'
            f'Seats: {len(self._participants)}/{self.capacity}'
        )


class Meeting(Event):
    def __init__(
            self,
            title: str,
            start: datetime,
            duration_minutes: int,
            organizer: Organizer,
            location: str = ''
    ) -> None:
        super().__init__(title, start, duration_minutes, location)

        self.organizer: Organizer = organizer
        self.attendees: list[Attendee] = []

    def add_attendee(self, name: str, email: str) -> None:
        attendee = Attendee(name, email)
        self.attendees.append(attendee)

    def confirm_attendee(self, email) -> None:
        for attendee in self.attendees:
            if attendee.email == email:
                attendee.confirm()
                return
        raise ValueError('Attendee email not found.')

    @override
    @staticmethod
    def category() -> str:
        return 'Meeting'

    @override
    def describe(self) -> str:
        attendees_text = (
            "\n".join(
                f"- {a.name} ({'✔' if a.confirmed else '❌'})"
                for a in self.attendees
            )
            if self.attendees
            else "No attendees"
        )

        return (
            f"Meeting: {self.title}\n"
            f"Organizer: {self.organizer.name}\n"
            f"Time: {self.start:%Y-%m-%d %H:%M} - {self.end:%H:%M}\n"
            f"Location: {self.location or 'N/A'}\n"
            f"Attendees:\n{attendees_text}"
        )


class Person:
    def __init__(
            self,
            name: str,
            email: str,
    ) -> None:
        self.name: str = name
        self.email: str = email


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError('Name cannot be empty.')
        self._name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if '@' not in value:
            raise ValueError('Invalid name.')

        self._email = value

    def __str__(self):
        return f'{self.name} ({self.email})'



class Organizer:
    def __init__(self):
        self.name = ''


class Attendee:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.confirmed = False

    def confirm(self):
        pass


