import random
from DemoQA.models.person_model import Person
from faker import Faker

faker_ru = Faker("ru_RU")
Faker.seed()


def generated_person():
    # Функция generated_person использует библиотеку faker для генерации
    # случайных данных о человеке на основе локализации на русский язык
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


def generated_file():
    # Функция создает случайный файл и записывает в него случайное сообщение.
    path = rf'C:\Users\Yan\Desktop\PythonAutomation\filetest' \
           rf'{random.randint(0, 999)}.txt'
    file = open(path, 'w+')
    file.write(f'Ola, amigo!{random.randint(0, 999)}')
    file.close()
    return file.name, path
