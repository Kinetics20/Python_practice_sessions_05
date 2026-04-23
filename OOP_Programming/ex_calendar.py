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


class Organizer(Person):
    def __init__(self, name: str, email: str, department: str) -> None:
        super().__init__(name, email)
        self.department: str = department


class Attendee(Person):
    def __init__(self, name: str, email: str) -> None:
        super().__init__(name, email)
        self.confirmed: bool = False

    def confirm(self) -> None:
        self.confirmed = True


class Calendar:
    def __init__(self, owner: str) -> None:
        self._owner: str = owner
        self._events: list[Event] = []

    def add_event(self, event: Event) -> None:
        self._events.append(event)
        self._events.sort(key=lambda x: x.start)

    def list_events(self) -> None:
        print(f'\nCalendar of {self._owner}')
        print('-' * 40)

        for event in self._events:
            print(event)

    def show_details(self) -> None:
        print('\nDetails')
        print('-' * 40)

        for event in self._events:
            print(event.describe())
            print()

    def find_conflicts(self) -> None:
        print('\nConflicts')
        print('-' * 40)

        for i in range(len(self._events)):
            for j in range(i + 1, len(self._events)):
                if self._events[i].overlap_with(self._events[j]):
                    print(f'{self._events[i].title} overlaps with {self._events[j].title}')


def main() -> None:
    calendar = Calendar('Mike')

    organizer = Organizer('Mike', 'sth@gmail.com', 'Python')

    meeting = Meeting(
        title='Agentic AI discussion',
        start=datetime(2026, 4, 22, 21, 30),
        duration_minutes=60,
        organizer=organizer,
        location='Lima'

    )

    meeting.add_attendee('Andrew', 'andrew@gmail.com')
    meeting.add_attendee('Greg', 'greg@gmail.com')
    meeting.add_attendee('Kate', 'kate@gmail.com')

    meeting.confirm_attendee('greg@gmail.com')
    meeting.confirm_attendee('kate@gmail.com')

    workshop = Workshop(
        title='Python OOP',
        start=datetime(2026, 4, 22, 21, 0),
        duration_minutes=240,
        instructor='Pablo',
        capacity=15,
    )

    workshop.register('Pete')
    workshop.register('Amos')
    workshop.register('Mateo')
    workshop.register('Richard')
    workshop.register('Agatha')
    workshop.register('Andrew')
    workshop.register('Ramon')

    calendar.add_event(workshop)
    calendar.add_event(meeting)

    calendar.list_events()
    calendar.show_details()
    calendar.find_conflicts()


if __name__ == '__main__':
    main()
