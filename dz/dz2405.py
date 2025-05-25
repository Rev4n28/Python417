class Student:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(self.name, "=>", end=" ")

    class Model:
        def __init__(self):
            self.brand = "HP"
            self.model = "i7"
            self.memory = 16

        def print_info(self):
            print(f"{self.brand}, {self.model}, {self.memory}")


s1 = Student("Roman")
s1.print_info()
h1 = s1.Model()
h1.print_info()

s2 = Student("Vladimir")
s2.print_info()
h2 = s2.Model()
h2.print_info()