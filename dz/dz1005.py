class Auto:

    def __init__(self, name, date, brand, power, color, price):
        self.name = name
        self.date = date
        self.brand = brand
        self.power = power
        self.color = color
        self.price = price

    def print_info(self):
        print(" Данные автомобиля ".center(40, "*"))
        print(f"Название модели: {self.name}\nГод выпуска: {self.date}\nПроизводитель: {self.brand}\n"
              f"Мощность двигателя: {self.power}\nЦвет машины: {self.color}\nЦена: {self.price}")
        print("=" * 40)

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_date(self, date):
        self.date = date

    def get_date(self):
        return self.date

    def set_brand(self, brand):
        self.brand = brand

    def get_brand(self):
        return self.brand

    def set_power(self, power):
        self.power = power

    def get_power(self):
        return self.power

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price


a1 = Auto("", "", "", "", "", "")
a1.print_info()

a1.set_name("X7 M50i")
a1.set_date("2021")
a1.set_brand("BMW")
a1.set_power("530 л.с.")
a1.set_color("white")
a1.set_price("10790000")
a1.print_info()
