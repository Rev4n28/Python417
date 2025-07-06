from models.database import Session, create_db

from faker import Faker
from database0607.people import People


def create_database(load_faker_data=True):
    create_db()
    if load_faker_data:
        _load_faker_data(Session())


def _load_faker_data(session):
    jobs_name = ['Frontend-разработчик',
                 'Backend-разработчик',
                 'Fullstack-разработчик',
                 'Системный администратор',
                 'Аналитик данных',
                 'Белый хакер',
                 'Веб-дизайнер']

    # group1 = Group(group_name='MDA-7')
    # group2 = Group(group_name='MDA-9')
    # session.add(group1)
    # session.add(group2)
    #
    # for key, it in enumerate(lessons_name):
    #     lesson = Lesson(lesson_title=it)
    #     lesson.groups.append(group1)
    #     if key % 2 == 0:
    #         lesson.groups.append(group2)
    #     session.add(lesson)

    faker = Faker('ru_RU')
    session.commit()

    for _ in range(50):
        full_name = faker.name().split()
        age = faker.random.randint(20, 75)
        job = faker.random.choice(jobs_name)
        people = People(full_name, age, job)
        session.add(people)

    session.commit()
    session.close()
