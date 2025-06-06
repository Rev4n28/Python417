class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetr(self):
        return self.a + self.b + self.c


if __name__ == '__main__':
    t1 = Triangle(10, 20, 30)
    t2 = Triangle(40, 50, 60)
    print(t1.perimetr())
    print(t2.perimetr())
