from models.database import Base
from sqlalchemy import Column, Integer, String


class People(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True)
    surname = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    patronymic = Column(String(250), nullable=False)
    age = Column(Integer)
    job = Column(String(250), nullable=False)

    def __init__(self, full_name, age, job):
        self.surname = full_name[0]
        self.name = full_name[1]
        self.patronymic = full_name[2]
        self.age = age
        self.job = job

    def __repr__(self):
        return (f"Человек (ФИО: {self.surname} {self.name} {self.patronymic}, Возраст: {self.age}, "
                f"Должность: {self.job})")
