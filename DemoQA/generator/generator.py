import random
from DemoQA.data.data import Person
from faker import Faker

faker_ru = Faker("ru_RU")
Faker.seed()


def generated_person():
    # ������� "generated_person()" ���������� ���������� "faker" ��� ���������
    # ��������� ������ � �������� �� ������ ����������� �� ������� ����
    # ("ru_RU").

    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " +
                  faker_ru.middle_name(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        age=random.randint(10, 80),
        salary=random.randint(50000, 100000),
        department=faker_ru.job(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
    )