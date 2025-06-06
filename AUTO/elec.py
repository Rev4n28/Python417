from auto import Auto


class Electro(Auto):
    def print_info(self):
        super().print_info()
        print("Этот автомобиль имеет мощность 100%")


def run():
    e = Electro("Tesla", "T", 2018, 99000)
    e.print_info()


run()
