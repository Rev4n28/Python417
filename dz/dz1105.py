from math import sqrt


class Area:
    count = 0

    @staticmethod
    def heron(a, b, c):
        p = (a + b + c) / 2
        if a + b <= c or a + c <= b or b + c <= a:
            print("Сумма длин двух сторон треугольника меньше или равна длине третьей стороны")
        elif a <= 0 or b <= 0 or c <= 0:
            print("Длина стороны треугольника не может быть меньше или равна 0")
        else:
            print(f"Площадь треугольника по формуле Герона ({a},{b},{c}):", sqrt(p * (p - a) * (p - b) * (p - c)))
            Area.count += 1

    @staticmethod
    def triangle(a, h):
        if a <= 0 or h <= 0:
            print("Длина стороны треугольника и его высота не может быть меньше или равна 0")
        else:
            print(f"Площадь треугольника через основание и высоту ({a},{h}):", (a * h) / 2)
            Area.count += 1

    @staticmethod
    def square(a):
        if a <= 0:
            print("Длина стороны квадрата не может быть меньше или равна 0")
        else:
            print(f"Площадь квадрата ({a}):", a ** 2)
            Area.count += 1

    @staticmethod
    def rectangle(a, b):
        if a <= 0 or b <= 0:
            print("Длина стороны прямоугольника не может быть меньше или равна 0")
        else:
            print(f"Площадь прямоугольника ({a},{b}):", a * b)
            Area.count += 1


count = f"Количество подсчётов площади: {Area.count}"
Area.heron(3, 4, 5)
Area.triangle(6, 7)
Area.square(7)
Area.rectangle(2, 6)
Area.heron(10, 20, 30)
print(count)
