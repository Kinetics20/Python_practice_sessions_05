from abc import ABC, abstractmethod
from typing import override


class Department:
    def __init__(self, name: str, location: str) -> None:
        self.name: str = name
        self.location: str = location

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        cleared = value.strip()
        if len(cleared) < 2:
            raise ValueError('Name must have at least 2 characters.')
        self._name = cleared

    @property
    def location(self) -> str:
        return self._location

    @location.setter
    def location(self, value: str) -> None:
        cleared = value.strip()
        if len(cleared) < 4:
            raise ValueError('Location name must have at least 4 characters.')
        self._location = cleared

    def department_info(self) -> str:
        return f'Department: {self.name}, {self.location}'


class Project:
    def __init__(self, name: str, budget: float) -> None:
        self.name: str = name
        self.budget: float = budget

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        cleared = value.strip()
        if len(cleared) < 2:
            raise ValueError('Name must have at least 2 characters.')
        self._name = cleared

    @property
    def budget(self) -> float:
        return self._budget

    @budget.setter
    def budget(self, value: float) -> None:
        if value < 10_000:
            raise ValueError('Budget must be at least 10,000.')
        self._budget = value

    def project_info(self) -> str:
        return f'Project: {self.name}, {self.budget}'


class Employee(ABC):
    def __init__(
            self,
            first_name: str,
            last_name: str,
            employee_id: str,
            salary: float
    ) -> None:
        self._first_name: str = first_name
        self._last_name: str = last_name
        self._employee_id: str = employee_id
        self.salary: float = salary

    @property
    def first_name(self) -> str:
        return self._first_name

    @property
    def last_name(self) -> str:
        return self._last_name

    @property
    def employee_id(self) -> str:
        return self._employee_id

    @property
    def salary(self) -> float:
        return self._salary

    @salary.setter
    def salary(self, value: float) -> None:
        if value < 1000:
            raise ValueError('Salary should be at least 1000.')
        self._salary = value

    @abstractmethod
    def work(self) -> str:
        ...

    def get_full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def employee_info(self) -> str:
        return f'Employee info: {self.get_full_name()}, {self.employee_id}, {self.salary}'


class ITEmployee(Employee):
    def __init__(
            self,
            first_name: str,
            last_name: str,
            employee_id: str,
            salary: float,
            department: Department,
            project: Project,
            programming_language: str

    ) -> None:
        super().__init__(first_name, last_name, employee_id, salary)
        self._department: Department = department
        self._project: Project = project
        self.programming_language: str = programming_language

    @property
    def department(self) -> Department:
        return self._department

    @property
    def project(self) -> Project:
        return self._project

    @property
    def programming_language(self) -> str:
        return self._programming_language

    @programming_language.setter
    def programming_language(self, value: str) -> None:
        cleared = value.strip()
        if len(cleared) < 2:
            raise ValueError('Programming language should contain 2 characters at least.')
        self._programming_language = cleared

    def assign_project(self, project: Project) -> None:
        self._project = project

    @abstractmethod
    def write_code(self) -> str:
        ...


class BackendDeveloper(ITEmployee):
    def __init__(
            self,
            first_name: str,
            last_name: str,
            employee_id: str,
            salary: float,
            department: Department,
            project: Project,
            programming_language: str,
            framework: str
    ) -> None:
        super().__init__(
            first_name,
            last_name,
            employee_id,
            salary,
            department,
            project,
            programming_language
        )
        self.framework: str = framework

    @property
    def framework(self) -> str:
        return self._framework

    @framework.setter
    def framework(self, value: str) -> None:
        cleared = value.strip()
        if len(cleared) < 2:
            raise ValueError("Framework name should contain at least 2 characters.")
        self._framework = cleared

    @override
    def work(self) -> str:
        return f'{self.get_full_name()} is working on the {self.project.name}.'

    @override
    def write_code(self) -> str:
        return f'{self.get_full_name()} is coding in {self.programming_language} using {self.framework}.'

    def design_api(self) -> str:
        return f'The {self.get_full_name()} is designing API for {self.project.name}.'


class PythonBackendDeveloper(BackendDeveloper):
    def __init__(
            self,
            first_name: str,
            last_name: str,
            employee_id: str,
            salary: float,
            department: Department,
            project: Project,
            framework: str,
            uses_fastapi: bool

    ) -> None:
        super().__init__(
            first_name,
            last_name,
            employee_id,
            salary,
            department,
            project,
            programming_language='Python',
            framework=framework,
        )
        self._uses_fastapi: bool = uses_fastapi

    @property
    def uses_fastapi(self) -> bool:
        return self._uses_fastapi

    @override
    def work(self) -> str:
        msg = super().work()
        return f'{msg} He specializes in Python backend development.'

    @override
    def write_code(self) -> str:
        return super().write_code()

    def create_fastapi_endpoint(self) -> str:
        if not self.uses_fastapi:
            raise ValueError('Python backend developer does not use FastAPI.')
        return f'{self.get_full_name()} is creating FastAPI endpoint using {self.framework}.'


class FrontendDeveloper(ITEmployee):
    def __init__(
            self,
            first_name: str,
            last_name: str,
            employee_id: str,
            salary: float,
            department: Department,
            project: Project,
            programming_language: str,
            frontend_framework: str
    ) -> None:
        super().__init__(
            first_name,
            last_name,
            employee_id,
            salary,
            department,
            project,
            programming_language,
        )
        self.frontend_framework: str = frontend_framework

    @property
    def frontend_framework(self) -> str:
        return self._frontend_framework

    @frontend_framework.setter
    def frontend_framework(self, value: str):
        cleared = value.strip()
        if len(cleared) < 2:
            raise ValueError('Name should have 2 characters at least.')
        self._frontend_framework = cleared

    @override
    def work(self) -> str:
        msg = super().work()
        return f'{msg} He is creating UI for {self.project.name}.'

    @override
    def write_code(self) -> str:
        return super().write_code()

    def build_ui_component(self) -> str:
        return f'{self.get_full_name()} is creating UI component for {self.project.name}'
