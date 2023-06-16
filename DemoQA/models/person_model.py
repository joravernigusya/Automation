from dataclasses import dataclass as model, dataclass


@model
class Person:
    # Модель данных для человека.
    full_name: str = None
    firstname: str = None
    lastname: str = None
    age: int = None
    salary: int = None
    department: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None


@dataclass
class Date:
    day: str = None
    month: str = None
    year: str = None
    time: str = None


@dataclass
class Color:
    color_name: list = None
