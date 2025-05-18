from abc import ABC, abstractmethod


class Human(ABC):
    def __init__(self, name, year):
        self.name = name
        self.year = year

    @abstractmethod
    def print_info(self):
        print(self.name, self.year, end=" ")


class Student(Human):
    def __init__(self, name, year, faculty, group, rating):
        super().__init__(name, year)
        self.faculty = faculty
        self.group = group
        self.rating = rating

    def print_info(self):
        super().print_info()
        print(self.faculty, self.group, self.rating, end=" ")


class Teacher(Human):
    def __init__(self, name, year, subject, skill):
        super().__init__(name, year)
        self.subject = subject
        self.skill = skill

    def print_info(self):
        super().print_info()
        print(self.subject, self.skill, end=" ")


class Graduate(Student):
    def __init__(self, name, year, faculty, group, rating, diploma):
        super().__init__(name, year, faculty, group, rating)
        self.diploma = diploma

    def print_info(self):
        super().print_info()
        print(self.diploma, end=" ")


h1 = Student("Батодалаев Даши", 16, "ГК", "Web_011", 5)
h2 = Student("Загидуллин Захар", 32, "РПО", "PD_011", 5)
h3 = Graduate("Шугани Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных")
h4 = Teacher("Даньшин Андрей", 38, "Астрофизика", 110)
h5 = Student("Маркин Даниил", 17, "ГК", "Python_011", 5)
h6 = Teacher("Башкиров Алексей", 45, "Разработка приложений", 20)

hs = [h1, h2, h3, h4, h5, h6]
for h in hs:
    h.print_info()
    print()
