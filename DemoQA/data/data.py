from dataclasses import dataclass as model


@model
class Person:
    # Это модель данных для человека.
    full_name: str = None
    firstname: str = None
    lastname: str = None
    age: int = None
    salary: int = None
    department: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None
