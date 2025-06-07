from abc import ABC, abstractmethod


class Auto(ABC):
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    @abstractmethod
    def print_info(self):
        print(f"{self.brand}, {self.model}, {self.year} год, {self.mileage} km")



