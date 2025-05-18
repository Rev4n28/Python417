# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, surname, num, percent, value):
#         self.__surname = surname
#         self.__num = num
#         self.__percent = percent
#         self.__value = value
#         print(f"Счёт #{self.__num} принадлежащий {self.__surname} был открыт.")
#         print("*" * 50)
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счёт {self.__num} принадлежащий {self.__surname} был закрыт")
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.__value} {Account.suffix}")
#
#     def print_info(self):
#         print("Информация о счёте:")
#         print("-" * 20)
#         print(f"#{self.__num}")
#         print(f"Владелец: {self.__surname}")
#         self.print_balance()
#         print(f"Проценты: {self.__percent:.0%}")
#         print("-" * 20)
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.__value, Account.rate_usd)
#         print(f"Состояние счёта: {usd_val} {self.suffix_usd}")
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.__value, Account.rate_eur)
#         print(f"Состояние счёта: {eur_val} {self.suffix_eur}")
#
#     def edit_owner(self, surname):
#         self.__surname = surname
#
#     def add_percent(self):
#         self.__value += self.__value * self.__percent
#         print("Проценты были успешно начислены")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.__value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.__value -= val
#             print(f"{val} {Account.suffix} было успешно снято!")
#         self.print_balance()
#
#     def add_money(self, val):
#         self.__value += val
#         print(f"{val} {Account.suffix} было успешно добавлено")
#         self.print_balance()
#
#     def get_surname(self):
#         return self.__surname
#
#     def set_surname(self, surname):
#         if isinstance(surname, str):
#             self.__surname = surname
#         else:
#             print("Изменяемая фамилия должна представлять собой строку")
#
#     def get_num(self):
#         return self.__num
#
#     def set_num(self, num):
#         if isinstance(num, str):
#             self.__num = num
#         else:
#             print("Изменяемый номер счёта должен быть в виде строки")
#
#     def get_percent(self):
#         return self.__percent
#
#     def set_percent(self, percent):
#         if isinstance(percent, float) and 0.01 < percent < 0.99:
#             self.__percent = percent
#         else:
#             print("Изменяемый процент должен представлять собой вещественное число от 0.01 до 0.99")
#
#     def get_value(self):
#         return self.__value
#
#     def set_value(self, value):
#         if isinstance(value, int):
#             self.__value = value
#         else:
#             print("Изменяемая сумма должна быть числом")
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#
# acc = Account("Долгих", "12345", 0.03, 1000)
#
# acc.set_surname("Черных")
# acc.set_num("09876")
# acc.set_percent(0.3)
# acc.set_value(2000)
#
# acc.print_info()
#
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# Account.set_usd_rate(2)
# Account.set_eur_rate(3)
#
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
#
# acc.edit_owner("Дюма")
# acc.print_info()
# print()
#
# acc.add_percent()
# print()
#
# acc.withdraw_money(3000)
# print()
#
# acc.withdraw_money(100)
# print()
#
# acc.add_money(5000)
# print()
#
# acc.withdraw_money(3000)
# print()

class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = "RUB"
    suffix_usd = "USD"
    suffix_eur = "EUR"

    def __init__(self, surname, num, percent, value):
        self.__surname = surname
        self.__num = num
        self.__percent = percent
        self.__value = value
        print(f"Счёт #{self.__num} принадлежащий {self.surname} был открыт.")
        print("*" * 50)

    def __del__(self):
        print("*" * 50)
        print(f"Счёт {self.__num} принадлежащий {self.surname} был закрыт")

    def print_balance(self):
        print(f"Текущий баланс {self.__value} {Account.suffix}")

    def print_info(self):
        print("Информация о счёте:")
        print("-" * 20)
        print(f"#{self.__num}")
        print(f"Владелец: {self.surname}")
        self.print_balance()
        print(f"Проценты: {self.__percent:.0%}")
        print("-" * 20)

    def convert_to_usd(self):
        usd_val = Account.convert(self.__value, Account.rate_usd)
        print(f"Состояние счёта: {usd_val} {self.suffix_usd}")

    def convert_to_eur(self):
        eur_val = Account.convert(self.__value, Account.rate_eur)
        print(f"Состояние счёта: {eur_val} {self.suffix_eur}")

    def edit_owner(self, surname):
        self.__surname = surname

    def add_percent(self):
        self.__value += self.__value * self.__percent
        print("Проценты были успешно начислены")
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.__value:
            print(f"К сожалению у вас нет {val} {Account.suffix}")
        else:
            self.__value -= val
            print(f"{val} {Account.suffix} было успешно снято!")
        self.print_balance()

    def add_money(self, val):
        self.__value += val
        print(f"{val} {Account.suffix} было успешно добавлено")
        self.print_balance()

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if isinstance(surname, str):
            self.__surname = surname
        else:
            print("Изменяемая фамилия должна быть представлена в виде строки")

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, num):
        if isinstance(num, str):
            self.__num = num
        else:
            print("Изменяемый номер счёта должен быть в виде строки")

    @property
    def percent(self):
        return self.__percent

    @percent.setter
    def percent(self, percent):
        if isinstance(percent, float) and 0.01 < percent < 0.99:
            self.__percent = percent
        else:
            print("Изменяемый процент должен представлять собой вещественное число от 0.01 до 0.99")

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if isinstance(value, int):
            self.__value = value
        else:
            print("Изменяемая сумма должна быть числом")

    @staticmethod
    def convert(value, rate):
        return value * rate

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate


acc = Account("Долгих", "12345", 0.03, 1000)

acc.surname = "Черных"
acc.num = "09876"
acc.percent = 0.3
acc.value = 2000

acc.print_info()

acc.convert_to_usd()
acc.convert_to_eur()
print()
Account.set_usd_rate(2)
Account.set_eur_rate(3)

acc.convert_to_usd()
acc.convert_to_eur()
print()

acc.edit_owner("Дюма")
acc.print_info()
print()

acc.add_percent()
print()

acc.withdraw_money(3000)
print()

acc.withdraw_money(100)
print()

acc.add_money(5000)
print()

acc.withdraw_money(3000)
print()
