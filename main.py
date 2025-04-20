# name = "5"
# age = 20
# print(name, type(name))
# print(age, type(age))
# print(int(name) + age)
import locale
import time

# a = 4  # комментарий
# b = 5
# print("a =", a, id(a))
# print("b =", b, id(b))
# a = b
# print("a =", a, id(a))
# print("b =", b, id(b))

# a = b = c = 5
# a, b, c = 5, "Hello", 9.2
# print(a)
# print(b)
# print(c)

# firstname = "admin"
# print(firstname)

# import keyword
#
# print(keyword.kwlist)

# PI = 3.14
# print(PI)
# PI = 2
# print(PI)

# a = 7
# b = 15
# print("a:", a)
# print("b:", b)
#
# # c = a # c = 1
# # a = b # a = 2
# # b = c # b = 1
# a, b = b, a
#
# print("a:", a)
# print("b:", b)

# print("строка \
# символов")
# print('строка символов \nстрока символов строка символов строка символов строка символов строка символов '
#       'строка символов')

# print("\tДокумент \"file.py\" находится \tпо     пути: \rD:\\folder\\file.py")

# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + " " + s2 + "___"
# print(s3)
# print(s3 * 3)

# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(6 ** 2)
# print(7 / 2)
# print(7 // 2)
# print(7 % 2)

# a, b, c = 5, 7, 3
# res = a + b + c
# print("Сумма чисел равна: ", res)
# print("Произведение чисел равно: ", a * b * c)
# print("Среднее арифметическое чисел равно: ", res / 3)

# number = (6 + 4) * (5 ** 2 + 7)
# print(number)

# num = 10
# num += 5
# print(num)  # 15
# num -= 3
# print(num)  # 12
#
# num *= 4
# print(num)  # 40


# num = 4321
# print("Исходное число:", num)
# a = num % 10
# print(a)
# b = (num % 100 - a) // 10
# print(b)
# c = (num % 1000) // 100
# print(c)
# d = num // 1000
# print(d)

# a = num % 10
# print("a:", a)
# num = num // 10
# # print(num)
# b = num % 10
# print("b:", b)
# num = num // 10
# # print(num)
# c = num % 10
# print("c:", c)
# num = num // 10
# # print(num)
# d = num % 10
# print("d:", d)
# print("Обратное число:", a * 1000 + b * 100 + c * 10 + d)

# num = 4321
# print("Исходное число:", num)
# res = num % 10 * 1000  # 1000
# num //= 10  # num = num // 10
# res += num % 10 * 100
# num //= 10
# res += num % 10 * 10
# num //= 10
# res += num
# print("Обратное число:", res)

# num1 = "2"
# num2 = 3
#
# # res = int(num1) + num2
# res = num1 + str(num2)
# print(res)
#
# print(int(2.987))
# print(round(2.587, 2))

# num1 = "2.5"
# num2 = 3
# res = float(num1) + num2
# print(res)
#
# name = "Виктор"
# age = 28
# print("Меня зовут", name, ". Мне", age, "лет")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет")
# print("Меня зовут ", name, ". Мне ", age, " лет", sep="", end="\n\n")
# print("Новая строка")

# name = input("Ваше имя: ")
# print("Hello,", name)

# num = int(input("Введите число: "))  # int("5")
# power = int(input("Введите степень: "))  # int("2")
# # print(num, type(num))
# # print(power, type(power))
# # num = int(num)
# # power = int(power)
# res = num ** power
# print("Число", num, "в степени", power, "равно:", res)

# b1 = True
# b2 = False
# # print(b1, type(b1))
# print(b1 + 5) # 1 + 5
# print(b2 + 5) # 0 + 5

# print(bool("python"))
# print(bool(" "))
# print(bool(""))  # false
# print(bool(5))
# print(bool(-5))
# print(bool(0))  # false
# print(bool(0.1))
# print(bool(0.0))  # false
# print(bool(True))
# print(bool(False))  # false
# print(bool(None))  # false


# test = None
# print(test, type(test))
# test = 5
# print(test, type(test))

# print(7 == 7)
# print(2 + 5 == 7 + 3)
# print(7 != 10 - 3)
# print(8 > 5)
# print(8 >= 8)
#
# print(8 < 5)
# print(8 <= 8)
#
# print("hello" > "H{hello")  # 104 > 72


# print(2 < 4 < 9)  # True && True -> True
# print(2 * 5 > 7 >= 4 + 3)  # True && True -> True
# print(3 * 3 <= 7 >= 2)  # False && True -> False

# print(5 - 3 == 2 and 1 + 3 == 4)  # True : True => True
# print(5 - 3 == 2 and 1 + 3 < 4)  # True : False => False
# print(5 - 3 > 2 and 1 + 3 == 4)  # False : True => False
# print(5 - 3 > 2 and 1 + 3 < 4)  # False : False => False
#
# print(5 - 3 == 2 or 1 + 3 == 4)  # True : True => True
# print(5 - 3 == 2 or 1 + 3 < 4)  # True : False => True
# print(5 - 3 > 2 or 1 + 3 == 4)  # False : True => True
# print(5 - 3 > 2 or 1 + 3 < 4)  # False : False => False
#
# print(not 9 - 7)  # not True -> False
# print(not 7 - 7)  # not False -> True


# cnt = 15
# if cnt < 10:
#     cnt += 1
#     print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешён")
#     print("Добро пожаловать")
# else:
#     print("Доступ запрещён")


# import this
# print(this)


# a = 35
# b = 25
#
# if a > b:
#     print("a > b")
# elif b > a:
#     print("b > a")
# else:
#     print("a == b")

# a = input("Введите первую сторону: ")
# b = input("Введите вторую сторону: ")
# c = input("Введите третью сторону: ")
#
# if a == b == c:
#     print("Треугольник равносторонний")
# elif a == b or a == c or b == c:
#     print("Треугольник равнобедренный")
# else:
#     print("Треугольник разносторонний")

# Вложенные условия

# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5):
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
#
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
#
# else:
#     print("Такого дня недели не существует")

# month = int(input("Введите номер месяца (цифрой): "))
# if 1 <= month <= 12:
#     print("Время года данного месяца - ", end="")
#     if month == 1 or month == 2 or month == 12:
#         print("зима")
#     elif 3 <= month <= 5:
#         print("весна")
#     elif 6 <= month <= 8:
#         print("лето")
#     elif 9 <= month <= 11:
#         print("осень")
# else:
#     print("Неверно указан номер месяца")

# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке", n, "ворон", end="")
#     if n == 1:
#         print("а")
#     elif 2 <= n <= 4:
#         print("ы")
#     elif 5 <= n <= 9 or n == 0:
#         print("")
# else:
#     print("Некорректное количество ворон")

# n = int(input("Введите количество копеек: "))
# if 0 <= n <= 99:
#     if 11 <= n <= 14:
#         print(n, "копеек")
#     else:
#         kop = n % 10
#         if kop == 1:
#             print(n, "копейка")
#         elif 2 <= kop <= 4:
#             print(n, "копейки")
#         elif 5 <= kop <= 9 or kop == 0:
#             print(n, "копеек")
# else:
#     print("Некорректное количество копеек")

# password = "admin"
#
# match password:
#     case "admin":
#         print("Администратор")
#     case "user":
#         print("Пользователь")
#     case _:
#         print("Пароль неверен")

# day = "вторник"
# time = 15
#
# match day:
#     case "понедельник" | "вторник" | "среда" | "четверг" | "пятница" if 9 <= time <= 12 or 14 <= time <= 17:
#         print("Рабочий день")
#     case "суббота" | "воскресенье":
#         print("Выходной день")
#     case _:
#         print("Такого дня недели не существует или не рабочее время")
#

# a, b = 20, 10
# print("a == b" if a == b else "a > b" if a > b else "a < b")

# a = 0
# b = "2"
# print(a+b)


# try:
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Что-то пошло не так")

# n = int(input("Введите целое число: "))
# print(n * 2)
# print("Код ниже")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки или нельзя делить на ноль")
# else:
#     print("Все нормально. Вы ввели", n, "и", m)
# finally:
#     print("Конец программы")


# n = input("Введите первое число: ")
# m = input("Введите второе число: ")
# try:
#     print(int(n) + int(m))
# except ValueError:
#     print(n + m)
# finally:
#     print("Конец программы")


# n = input("Введите первое число: ")
# m = input("Введите второе число: ")
#
# try:
#     n = int(n)
#     m = int(m)
# except ValueError:
#     n = str(n)
# finally:
#     print(n + m)


#  цикл while

# i = 0
# while i < 5:
#     print("i = ", i)
#     i += 1

# Итерация - один шаг цикла

# i = 1
# while i <= 20:
#     print(i + 1, end=" ")
#     i += 2

# n = int(input("Введите количество символов: "))
# print("+-" * n)

# i = 0
# while i < n:
#     if i % 2 == 0:
#         print("+", end="")
#     else:
#         print("-", end="")
#     i += 1


# i = 0
#
# while n > 0:
#     if n % 2:
#         print("+", end="")
#     else:
#         print("-", end="")
#     n -= 1


# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите конец диапазона: "))
# res = 0
# while a <= b:
#     if  a % 2:
#         print(a, end=" ")
#         res += a
#     a += 1
# print("Сумма нечётных элементов:", res)


# n = input("Введите целое число: ")
#
# while type(n) is not int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое")
#         n = input("Введите целое число: ")
# if n % 2 == 0:
#     print("Чётное")
# else:
#     print("Нечётное")


# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершён!")

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1


# res = 1
# while True:
#     n = int(input("Введите положительное число: "))
#     if n == 0:
#         break
#     res *= n
#
#
# print(res)


# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)

# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j =", j)
#         j += 1
#     i += 1

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if j % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1


# i = 0
# while i < 5:
#     j = 0
#     while j < i:
#         print(" ", end="")
#         j += 1
#     print("*")
#     i += 1

# i = 0
# while i < 5:
#     print(" " * i, "*", sep="")
#     i += 1

# print()
# print("*" * 0)

# num = int(input("Количество символов: "))
# sym_type = input("Тип символа: ")
# orient = int(input("0 - горизонтальная \n1 - вертикальная \nОриентация: "))
# i = 0
# while i <= num:
#     if orient == 0:
#         print(sym_type, end="")
#     elif orient == 1:
#         print(sym_type, end="\n")
#     else:
#         print("Указано некорректное значение ориентации")
#     i += 1

# for element in collection:
#     print(element)

# for i in "Hello", "World":
#     print(i)

# range(start, stop, step) # start=0, step=1
# print(range(1, 9, 2))
#
# for i in range(10, -1, -2):
#     print(i, end=" ")
#
# print()
#
# i = 10
# while i >= 0:
#     print(i, end=" ")
#     i -= 2
#
#     print()
#
# i = 2
# while i < 10:
#     print(i, end=" ")
#     i += 3

# print()
#
# ch = int(input("Введите целое число: "))
#
# for i in range(1, ch + 1):
#     if  ch % i == 0:
#         print(i, end=" ")

# for i in range(10, 100):
#     if i % 11 == 0:
#         print(i, end=" ")
# print()
# for i in range(11, 100, 11):
#     print(i, end=" ")
# print()
# for i in range(10, 100):
#     if i % 10 == i // 10:
#         print(i, end=" ")

# for i in range(3):
#     if i == 1:
#         continue
#     print(i)
# else:
#     print("Конец цикла")

# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("-----")

# w = int(input("Введите длину прямоугольника: "))
# h = int(input("Введите ширину прямоугольника: "))
#
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# st = [i * 2 for i in "Hello"]
# print(st)
#
# num = [i for i in range(30) if i % 2 == 0]
# print(num)


# Список (list)

# num = [14, 16, 18, 20, 22, 24, 26, 28, "Hello", True, 2.8]
# print(num)
# # print(type(num))
# # print(num[-1])
# # print(num[-3])
# # num[0] = 256
# # print(num)
# # num[1] += 100
# # print(num)
# print(len(num))
# print(num[-1])
# print(num[11])

# s = []
# print(s, type(s))
#
# s2 = list("Hello")
# print(s2, type(s2))

# s1 = [1, 2, 3]
# s2 = [4, 5, 6]
# s3 = s1 + s2
# print(s3)
# print(s3 * 3)

# n = list(range(10))
# print(n)
# n = list(range(2, 10))
# print(n)
# n = list(range(10, 2, -2))
# print(n)

# [выражения for переменная in последовательность]

# a = [0 for i in range(5)]
# print(a) # [0, 0, 0, 0, 0]
#
# n = 5
# a = [i for i in range(n + 1)]
# print(a) # [0, 1, 2, 3, 4]

# a = [0] * int(input("Введите кол-во элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)

# a = [input("-> ") for i in range(int(input("n: ")))]
# print(a)

# lst = [5, 9, 8, 2, 3]
#
# for i in range(len(lst)):  # 0 1 2 3 4
#     print(lst[i], end=" ")
#
# print()
#
# for i in lst:
#     print(i, end=" ")


# a = [0] * int(input("Введите кол-во элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)

# a = [int(input("-> ")) for i in range(int(input("n: ")))]
# print(a)
# s = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         s += a[i]
# print("Сумма отрицательных элементов: ", s)

# a = [int(input("-> ")) for i in range(int(input("n: ")))]
# print(a)
# s = 0
# for i in a:
#     if i < 0:
#         s += i
#
# print("Сумма отрицательных элементов: ", s)

# n = list(range(21, 41))
# print(n)
# s = 0
# k = 0
# for i in range(len(n)):
#     if n[i] % 2:
#         s += n[i]
#     else:
#         k += 1
# print("Количество чётных элементов: ", k)
# print("Сумма нечётных элементов: ", s)

# n = list(range(21, 41))
# print(n)
# s = 0
# k = 0
# for i in n:
#     if i % 2:
#         s += i
#     else:
#         k += 1
# print("Количество чётных элементов: ", k)
# print("Сумма нечётных элементов: ", s)


# a = [int(input("-> ")) for i in range(int(input("n: ")))]
# print(a)
# for i in range(len(a)):
#     if i % 2 == 0:
#         print(a[i], end=" ")


# a = [int(input("-> ")) for i in range(int(input("n: ")))]
# print(a)
# for i in range(0, len(a), 2):
#     print(a[i], end=" ")


# a = [int(input("-> ")) for i in range(int(input("n: ")))]
# print(a)
# for i in a:
#     if i % 2 == 0:
#         print(i, end=" ")


# a = [int(input("-> ")) for i in range(int(input("n: ")))]
# print(a)
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=" ")

# a = [int(input("-> ")) for i in range(int(input("n: ")))]
# print(a)
# j = a[0]
# for i in a:
#     if i > j:
#         print(i, end=" ")
#     j = i

# Срез
# Список[start:stop:step]
# lst = [3, 7, 4, 6, 2]
# print(lst[1:3])
# print(lst[1:])
# print(lst[:4])
# print(lst[::-1])
# print(lst[3:1:-1])
# print(lst[10:20])

# lst = list(range(1, 8))
# print(lst)
# print(lst[::-1])
# print(lst[::2])
# print(lst[1::2])
# print(lst[:1])
# print(lst[-1:])
# print(lst[6:])
# print(lst[3:4])
# print(lst[4:])
# print(lst[4:1:-1])
# print(lst[2:5])

# st = "HelloWorld"
# print(st[1:5])
# print(st[::-1])

# s = [5, 9, 3, 7, 1, 8]
# print(s)
# s[1:3] = [0, 0, 0, 0]
# print(s)
# s[1:2] = [20]
# print(s)
# s[2] = 120
# print(s)
# s[10:11] = [200]
# print(s)
# print(len(s))


# print(dir(list))

# Методы списков
# s = [5, 20, 120, 200]
# print(s)
# s.append(99)  # добавляет элемент в конец списка
# print(s)
# s.extend([1, 2, 3])  # добавляет список в конец списка
# print(s)
# s.insert(2, 100)  # добавляет элемент в список по заданному индексу
# print(s)
#
# lst = []
# n = int(input("Кол-во элементов списка: "))
# for i in range(n):
#     x = int(input("Введите число: "))
#     # lst.append(x)
#     lst.insert(0, x)
# print(lst)

# a = [5, 9, 2, 1, 4, 3]
# b = [4, 2, 1, 7, 3]
# c = []  # [2, 1, 4, 3]

# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break

# a = [5, 9, 2, 1, 4, 3, 4, 2]
# b = [4, 2, 1, 7, 3, 2]
# c = []  # [2, 1, 4, 3]
#
# for i in a:
#     if i in b and i not in c:
#         c.append(i)
# print(c)

# a = [1, 2, 3, 4, 5]
# b = [11, 22, 33]
# c = []

# if len(b) > len(a):
#     for i in range(len(a)):  # 0 1 2
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# else:
#     for i in range(len(b)):  # 0 1 2
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
#
# print(c)

# s = [5, 20, 120, 200, 120]
# print(s)
# s[2:] = []
# s[1:3] = []
# del s[1:3]
# s.remove(120) # удаляет (первое вхождение) элемент из списка по значению
# num = 3
# if num in s:
#     s.remove(num)
# s.pop()  # удаляет последний элемент из списка
# ind = 3
# try:
#     num = s.pop(ind)  # удаляет элемент по заданному индексу
# except IndexError:
#     print(ind, "- такого индекса не существует")

# s.clear()
# print(s)
# print(num)

# print("Введите элементы списка: ")
# a = [int(input("-> ")) for i in range(int(input("n: ")))]
# print(a)
# print("Введите индекс: ")
# k = int(input("k = "))
# try:
#     a.pop(k)
# except IndexError:
#     print("Элемент удалить не удалось.", k, "- такого индекса не существует")
# print(a)


# s = [5, 20, 120, 200, 120]
# print(s)
#
# num = s.count(20)  # кол-во заданных значений в списке
# print(num)
#
# ind = s.index(120, 3, 4)  # вернёт индекс первого вхождения заданного значения
# print(ind)

# a = [1, 2, 3]
# b = a.copy()
# print("a =", a)
# print("b =", b)
#
# a.append(20)
# print("a =", a)
# print("b =", b)
#
# b.append(200)
# print("a =", a)
# print("b =", b)

# b = [51, 32, 3, 200]
# print(b)
# # b.reverse()
# b.sort()  # reverse=True
# print(b)
#
# s = ["Виталий", "Сергей", "Александр", "Анна"]
# print(s)
# s.sort(key=len, reverse=True)
# print(s)
# print()
# c = [51, 32, 3, 200]
# print(c)
# lst = sorted(c)
# print(c)
# print(lst)

# Генерация случайных данных

# import random

# print(dir(random))
#
# print(random.random())
# print(random.randint(0, 9))
# print(random.randrange(2, 9, 2))
# print(round(random.uniform(10.5, 20.5), 2))

# city = ["Москва", "Новосибирск", "Воронеж", "Сочи", "Екатеринбург"]
# s = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# print(random.choice(city))
# print(random.choice(s))
#
# print(random.choices(city, k=3))
# print(random.choices(s, k=3))
#
# random.shuffle(city)
# print(city)
# random.shuffle(s)
# print(s)

# import random
#
# mas = [random.randint(20, 40) for i in range(10)]
# print(mas)

# lst = [34, 32, 20, 38, 35, 36, 33, 29, 32, 40]
# print(lst)
# print(len(lst))
# print(min(lst))
# print(max(lst))
# print(sum(lst))
#
# lst = ["Москва", "Новосибирск", "Воронеж", "Сочи", "Екатеринбург"]
# print(lst)
# print(len(lst))
# print(min(lst))
# print(max(lst))
# print(sum(lst))

# import random
# lst = [random.randint(0, 100) for i in range(10)]
# print(lst)
# max_1 = max(lst)
# print("MAX =", max_1)
# lst.remove(max_1)
# lst.insert(0, max_1)
# print(lst)

# import random
# lst = [random.randint(0, 100) for i in range(10)]
# print(lst)
# min_1 = min(lst)
# print("MIN =", min_1)
# ind = lst.index(min_1)
# print("INDEX =", ind)
# del lst[0:ind]
# print(lst)

# import random
# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# a = [random.randint(0, 10) for i in range(n1)]
# b = [random.randint(0, 10) for j in range(n2)]
# print("Первый список: ", a)
# print("Второй список: ", b)
# c = a + b
# print("Третий список: ", c)

# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
#
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
# print("Третий список: ", c)

# c = []
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
# print("Третий список: ", c)

# c = [min(a), min(b), max(a), max(b)]
# print("Третий список: ", c)

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# print(m)
# print(len(m))
# print(m[1][2])
# print(m[2][2])
#
# st = ["Hello", "World"]
# print(st[1][4])
# print("Вариант 1")
# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t\t")
#     print()
#
# print("Вариант 2")
# for i in m:
#     # print(i)
#     for j in i:
#         print(j, end="\t\t")
#     print()


# from math import pi
#
# # print(pi)
#
# radius = int(input("Введите радиус окружность: "))
# print("Длина окружности:", round(2 * pi * radius, 2))

import time


# print(time.time())
# print(time.ctime(7526407068))
# print(time.localtime())
# res = time.localtime()
# print(res.tm_year)
# print(time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime(26407068)))
# print(time.strftime("Today is %B %d, %Y."))
# locale.setlocale(locale.LC_ALL, "ru")
# print(time.strftime("Сегодня: %B %d, %Y."))
#
# num = 1_000_000.0
# print(num)  # 1'000'000.0

# pause = 1.5
# print("Программа запущена")
# time.sleep(pause)
# print(pause, "seconds")

# start = time.time()
# time.sleep(5)
# finish = time.time() - start
# print(finish)

# Function
# print()


# def hello(name, age):
#     print("Меня зовут:", name, "Мне", age, "лет")
#
#
# hello("Irina", 20)
# hello(19, "Ivan")

# def get_sum(a, b):
#     print("Сумма чисел: ", end="")
#     return a + b
#
#
# x = 2
# y = 5
# # get_sum(x, y)
# # get_sum(12, 7)
# # get_sum("abc", "def")
#
# res = get_sum(x, y)
# print(res * 2)


# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst
#     # return lst[::-1]


# def change(lst):
#     end = lst.pop()
#     start = lst.pop(0)
#     lst.append(start)
#     lst.insert(0, end)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с", "л", "о", "н"]))

# def test(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# # print(test(10, 5))
# # print(test(5, 10))
# num1 = 10
# num2 = 15
# if test(num1, num2):
#     print(num1, ">", num2)
# else:
#     print(num1, "<", num2)

# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_number = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         if "a" <= ch <= "z":
#             has_lower = True
#         if "0" <= ch <= "9":
#             has_number = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_number:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Это надёжный пароль")
# else:
#     print("Это ненадёжный пароль")

# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# print(get_sum(1, 5, d=2))

# def display_info(name, age):
#     print("Name:", name, "\nAge", age)
#
#
# display_info("Ira", 33)
# display_info(23, "Ira")
# display_info(age=23, name="Ira")

# a = "Hello"
# b = "Hello"
# print(a, id(a))
# print(b, id(b))
# print(a == b)
# print(a is b)
#
#
# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(lt1, id(lt1))
# print(lt2, id(lt2))
# print(lt1 == lt2)
# print(lt1 is lt2)

# lt1 = [1, 2, 3]
# print(lt1, id(lt1))
# lt1.append(4)
# print(lt1, id(lt1))
# lt1.pop(1)
# print(lt1, id(lt1))

# s = "Hello"
# print(s, id(s))
# # s = s + "!"
# s += "!"
# print(s, id(s))

# a = 5
# print(a, id(a))
# a += 0
# print(a, id(a))

# def test(lst):
#     lst.append(4)
#
#
# x = [1, 2, 3]
# print(test(x))
# print(x)
#
#
# def test1(n):
#     n = 5
#
#
# x1 = 3
# print(test1(x1))
# print(x1)

# Кортежи (tuple)

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# print(lst[1])
# print(tpl[1])
#
# lst[1] = 50
# tpl[1] = 50


# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)  # 1
#             second = tpl.index(el, first + 1) + 1
#             return tpl[first:second]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return tuple()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))


# from random import randint
#
#
# def ran(a, b):
#     return tuple(randint(a, b) for i in range(10))
#
#
# tpl1 = ran(0, 5)
# print(tpl1)
#
# tpl2 = ran(-5, 0)
# print(tpl2)
#
# tpl3 = tpl1 + tpl2
# print(tpl3)
# print("0 =", tpl3.count(0))


# point = (10, 20)
#
# match point:
#     case (0, 0):
#         print("Точка находится в координате 0:0")
#     case (x, y):
#         print("Точка находится в", 0, "по оси X и в", y, "координат по оси Y")
#     case (x, 0):
#         print("Точка находится в", x, "по оси X и в 0 координат по оси Y")
#     case (0, y):
#         print("Точка находится в 0 по оси X и в", y, "координат по оси Y")
#     case _:
#         print("Это не координаты точки")

# t = (10, "Python", (1, 2, 3), [4, 5, 6], ["hello", "world"])
# print(t)
# t[4][0] = "new"
# print(t)
# t[4].append("hi")
# print(t)


# Распаковка кортежа

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# # x, y, z = t
# x, y, z = 1, 2 ,3
# print(x, y, z)

# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# # user = get_user()
# # print(user)
# # first_name, year, married = user
# first_name, year, married = get_user()
# print(first_name, year, married)

# t = (1, 2, 3)
# del t
# print(t)

# t = (1, 2, 3, 4, 5)
# print(t, type(t))
# lst = list(t)
# print(lst, type(lst))
# lst.append(6)
# print(lst, type(lst))
# tpl = tuple(lst)
# print(tpl, type(tpl))

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
# print(countries, end="\n\n")
#
# for country in countries:
#     country_name, country_population, cities = country
#     print("\nСтрана:", country_name, ", население = ", country_population, sep="")
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород: ", city_name, ", население = ", city_population, sep="")
#

# s = input("Введите по порядку, без пробелов элементы кортежа: ")
# tpl = tuple(s)
# print(tpl)
#
# lst = []
# for i in range(len(tpl)):
#     if tpl[i] not  in lst:
#         lst.append(tpl[i])
#
# print(lst)
#
# for i in range(len(lst)):
#     print("Количество", lst[i], "=", tpl.count(lst[i]))
# 0
# s = one, two, three,
# зшт
# a = ()
# print(a, type(a))
# b = set()
# print(b, type(b))

# a = {}
# print(a, type(a))
# b = set("Hello")
# print(b, type(b))
# s = str(b)
# print(s)

# s = {x * x for x in range(10)}
# print(s)

# s = {input("-> ") for x in range(10)}
# print(s)
#
# s = {"one", "two", "three"}
# print("two" in s)
# print("four" in s)

# lst = ["ab_1", "ac_2", "bc_1", "bc_2"]
# print([i for i in lst if 'a' in i])
# # print(tuple(i for i in lst if "a" in i))
# # print({i for i in lst if "a" in i})
# print(["A" + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in lst])
# # print(tuple(["A" + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in lst]))
# # print({"A" + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in lst})
# print(["A" + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in lst if i[1] == 'c'])
# print(tuple("A" + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in lst if i[1] == 'c'))
# print({"A" + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in lst if i[1] == 'c'})


# for i in lst:
#     if i[1] == 'c':
#         if i[0] == 'a':
#             print("A" + i[1:])
#         else:
#             print("B" + i[1:])

# s = {"one", "two", "three"}
# s.add("four")  # добавляет элемент в множество
# print(s)
# # s.remove("four")
# # print(s)
#
# # el = "two"
# # if el in s:
# #     s.remove(el)  # удаляет элемент по значению, может выбрасываться исключение KeyError
# #
# # print(s)
# # s.discard("five")  # удаляет элемент по значению, исключение не выбрасывается при отсутствии
# # print(s)
#
# s.clear()  # очищает множество
# print(s)


# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# # # c = a.union(b)
# # c = a | b
# # print(c)
# # c = a & b
# # print(c)
# # c = a - b
# # print(c)
# c = a ^ b
# print(c)
# # a &= b
# # print(a)
# # a |= b
# # print(a)


# s1 = "Hello"
# s2 = "How are you"
# s3 = set(s1) & set(s2)
# print(s3)
# for i in s3:
#     print(i, end=" ")

# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# print(a >= b)
# print(a <= b)


# a = {3, 4, 0, 1, 2}
# print(a, type(a))
# lst = list(a)
# print(lst, type(lst))
# # lst = tuple(a)
# # print(lst, type(lst))
# b = set(lst)
# print(b, type(b))


# s = frozenset("hello")
# print(s)
# s = frozenset(["hello", "world"])
# print(s)
#
# a = frozenset({i ** 2 for i in range(10)})
# print(a)

# Словарь (dict)

# lst = [1, 2, 3]
# d = {"one": 1, "two": 2, "three": 3}
# print(lst, type(lst))
# print(d, type(d))
# print(lst[1])
# print(d["two"])
# d["two"] = 200
# print(d, type(d))

# d = {"one": 1, "two": 2}
# print(d, type(d))
#
# d1 = dict(one=1, two=2)
# print(d1, type(d1))


# def func(one, two):
#     return one, two
#
#
# print(func(two=1, one=2))


# lst = [["one", 1], ["two", 2], ["three", 3]]
#
# print(lst)
# print(dict(lst))

# d = {0: [5, 6, 7], True: 1, (1, 2): "кортеж", "список": [5, 6, 7], 1: 10, False: 0}
# print(d)
# print(d["список"][1])
# print(d[(1, 2)])
# print(d[0][0])

# d = {i * 2: i ** 2 for i in range(7)}
# print(d)

# from random import randint

# d = {input("-> "): input("-> ") for i in range(7)}
# print(d)

# d = {randint(1, 10): randint(50, 100) for i in range(7)}
# print(d)
#
# d = {"one": 1, "two": 2, "three": 3}
# # print("one" in d)
# # print(2 in d)
# key = "two"
# try:
#     print(d[key])
# except KeyError:
#     print("Элемента с ключом", key, "нет в словаре")
# # print(d)
#
# # for key in d:
# #     print(key, d[key])


# d = {i + 1: input("-> ") for i in range(4)}
# print(d)
# veg_del = int(input("Какой элемент исключить: "))
# del (d[veg_del])
# print(d)


# goods = {
#     "1": ["Core-i3-4330", 9, 4500],
#     "2": ["Core-i5-4670K", 3, 8500],
#     "3": ["AMD FX-6300", 4, 3700],
#     "4": ["Pentium G3220", 8, 2100],
#     "5": ["Core-i5-3450", 5, 6400],
# }
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")
#
# while True:
#     n = input("№: ")
#     if n != "0":
#         if n in goods:
#             while True:
#                 try:
#                     count = int(input("Количество: "))
#                     while True:
#                         if count > 0:
#                             goods[n][1] += count
#                             break
#                         else:
#                             print("Количество должно быть положительным числом")
#                             count = int(input("Количество: "))
#                     break
#                 except ValueError:
#                     print("Значение некорректною. Введите число")
#         else:
#             print("Такого ключа не существует")
#     else:
#         break
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")

# print(dir(dict))
#
# d = {"one": 1, "two": 2, "three": 3}
#
# print(d.keys())
# print(d.values())
# print(d.items())
#
# print(list(d.keys()))
# print(list(d.values()))
# print(list(d.items()))
#
# for i in d:
#     print(i, end=" ")
# print()
# for i in d.keys():
#     print(i, end=" ")
# print()
# for i in d.values():
#     print(i, end=" ")
# print()
# for i in d.items():
#     print(i, end=" ")
# print()
# for i, j in d.items():
#     print(i, ":", j)


# d = {"one": 1, "two": 2, "three": 3}
# d2 = d.copy()
# print("D =", d)
# print("D2 =", d2)
# d2["two"] = 200
# print("D =", d)
# print("D2 =", d2)
# d["four"] = 4
# print("D =", d)
# print("D2 =", d2)

# d = {"one": 1, "two": 2, "three": 3}
# # print(d["three"])  # KeyError
# # value = d.get("three2", "Такого элемента в словаре нет")
# # value = d.get("three2", False)
# # value = d.pop("two1", "Такого ключа не существует")
# # item = d.popitem()
# # print(item)
# # print(d)
# # d.clear()
# # item = d.setdefault("four", 4)
# # item = d.setdefault("two1", 4)
# # print(item)
# print(d)
#
# # d2 = {"four": 4, "five": 5, "two": 22}
# d2 = [("four", 4), ("five", 5), ("two", 22)]
# print(d2)
# # d3 = d | d2
# # print(d3)
#
# d.update(d2)
# print(d)


# d = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New York"
# }
# new_d = dict()
# new_d["name"] = d.pop("name")
# new_d["salary"] = d.pop("salary")
#
# print(d)
# print(new_d)

# d = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New York"
# }
# d["location"] = d.pop("city")
# print(d)

# s = {
#     "first": {
#         1: "one",
#         2: "two",
#         3: "three"
#     },
#     "second": {
#         4: "four",
#         5: "five"
#     }
# }
#
# print(s)
#
# for x in s:
#     print(x)
#     for y in s[x]:
#         print("\t", y, ":", s[x][y], sep="")
# print()
#
# for x, y in s.items():
#     print(x)
#     for i, j in y.items():
#         print("\t", i, ": ", j, sep="")

# d = {"один": 1, "два": 2, "три": 3, "четыре": 4}
# print({key: value for key, value in d.items()})
# print({value: key for key, value in d.items()})
#
# print({key: value for key, value in d.items() if value <= 2})
# print(slice(1, 3, None))


# d = {"один": 1, "два": 2, "три": 3, "четыре": 4}
# print(list(d))
# print(list(d.keys()))
# print(list(d.values()))
# print(list(d.items()))


# a = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
# d = dict()
# s = None
#
# for i in a:
#     if type(i) is str:  # type(i) == str
#         d[i] = []
#         s = i
#     else:
#         d[s].append(i)
#
#
# print(d)


# a = ["Декабрь", "Январь", "Февраль", "Март"]
# b = [12, 1, 2, 3]
# c = [1.0, 2.0, 3.0]
# print(dict(zip(b, a)))
# print(list(zip(a, b)))
# print(tuple(zip(a, b, c)))
# # print(list(zip(a)))

# month = [("Декабрь", 12), ("Январь", 1, 4), ("Февраль", 2), ("Март", 3)]
# a, b = zip(*month)
# print(a)
# print(b)


# one = {"name": "Irina", "surname": "Petrova", "job": "Consultant"}
# # two = {"name": "Igor", "surname": "Vetrov", "job": "Manager"}
# #
# # for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
# #     print(k1, "->", v1)
# #     print(k2, "->", v2)
#
# print(sorted(one.items()))

# letters = ["b", "a", "c", "d"]
# numbers = [3, 4, 1, 2]
#
# lst = list(zip(letters, numbers))
# print(lst)
# lst.sort()
# print(lst)
# print(dict(lst))
#
# lst1 = list(zip(numbers, letters))
# print(lst)
# lst1.sort()
# print(lst)
# print(dict(lst1))
# print({v: k for k, v in lst1})


# a = ["1", "2", "3"]
# # b = [*a, 4, 5, 6]
# # print(b)
# print(*a)
# # print(type(*a))
#
# one = {"one": 1, "two": 2}
# two = {"three": 4, "four": 4, "two": 22}
# print({**one, **two})
# print({**one})


# a = ["Январь", "Февраль", "Март"]
# i = 1
# for value in a:
#     print(i, ") ", value, sep="")
#     i += 1
# print()
# for i, value in enumerate(a, start=1):
#     print(i, ") ", value, sep="")


# one = {"name": "Irina", "surname": "Petrova", "job": "Consultant"}
#
# for i, (k, v) in enumerate(one.items()):
#     print(i, ") ", k, ": ", v, sep="")


# def func(*args):
#     return args
#
#
# print(func(5))
# print(func(5, 6, 7))
# print(func())


# def summa(*params):
#     res = 0
#     for i in params:
#         res += i
#     return res
#
#
# print(summa(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
# print(summa(7, 8, 9, 10))


# def search(*args):
#     average = sum(args) / len(args)
#     print(average)
#
#     res = []
#     for num in args:
#         if num < average:
#             res.append(num)
#     return res
#
#
# print(search(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(search(3, 6, 1, 9, 5))


# def func(a, *args):
#     return a, *args
#
#
# print(func(5))
# print(func(5, 1, 2, 3, 4))


# def print_scors(student, *scores):
#     print("Student Name:", student, end=". Score: ")
#     for score in scores:
#         print(score, end=", ")
#     print()
#
#
# print_scors("Irina", 100, 95, 88, 92, 99)
# print_scors("Igor", 96, 20, 33, 56)
# print_scors("Nikita")


# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(one="один"))


# def info(**data):
#     for k, v in data.items():
#         print(k, ": ", v, sep="")
#     print("\n")
#
#
# info(name="Irina", surname="Vetrova", age=22, phone="22-33-44")
# info(name="Igor", age=25, phone="99-88-77", email="igor@mail.ru")


# def func(a, b, *args, m=100, n=10, **kwargs):
#     print(args[0])
#     print(kwargs['c'])
#     return a, b, args, kwargs, m, n
# print(func(5, 1, 2, 3, 4, 5, 6, n=20, c=47, m=200, d=53, e=79))


# Области видимости (scope)

# name = "Tom"  # глобальная
#
#
# def hi():
#     global name, surname
#     name = "Same"
#     surname = "Jonson"  # локальная переменная
#     print("Hello", name, surname)
#
#
# def bye():
#     print("Good bye", name)
#
#
# hi()
# bye()
#
#
# print(name)
# hi()
# bye()
# print(surname)

#
# import builtins
#
# names = dir(builtins)
#
# for t in names:
#     print(t)
#

# prints = 5
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# print(max(lst))


# def add(a):
#     x = 2
#
#     def inner():
#         print("x =", x)
#         return a + x
#
#     return inner()
#
#
# print(add(3))
# # print(inner())


# def outer(who):
#     def inner():
#         print("Hello", who)
#
#     inner()
#
#
# outer("World")


# def outer():
#     a = 6  # 2
#
#     def inner(b):
#         a = 4  # 5
#         print("Сумма:", a + b)  # 6
#
#     print("a =", a)  # 3
#     inner(5)  # 4
#
#
# outer()  # 1


# x = 25
# t = 0
#
#
# def fn():
#     global t
#     a = 30  # 35
#
#     def inner():
#         nonlocal a
#         a = 35
#         # print("a =", a)
#
#     inner()
#     t = a
#
#
# fn()
#
# c = x + t  # 25 + 30 => 55  # 25 + 35 => 60
# print(c)


# def fn1():
#     x = 25
#
#     def fn2():
#         x = 33  # 55
#         d = x
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print("fn2.x =", x)  # 33
#         print("d", d)
#
#     fn2()
#     print("fn1.x =", x)  # 25


# fn1()
# print(x)
#
# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#         # print(a, b)
#
#     inner()
#     return [a, b]
#
# print(outer(2, 3, -1, 4))


# def func1():
#     a = 1
#     b = "Line"
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         print(a)
#         a = a + 1
#         b = b + "!"
#         return a, b, c
#
#     return func2()
#
#
# print(func1())


# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# p1 = outer(5)
# print(p1(10))
# print(p1(11))
#
# p2 = outer(6)
# print(p2(4))
#
#
# print(outer(5)(4))


# def func(city):
#     count = 0
#
#     def inner():
#         nonlocal count
#         count += 1
#         print(city, count)
#
#     return inner()
#
#
# res1 = func("Москва")
# print(res1)
# res1()
# res1()
# res1()
# res1()
# res2 = func("Сочи")
# res2()
# res2()
# res2()
#
# res1()
# res1()

# def func(x, y):
#     res = x + y
#     return res
#
#
# print(func(3, 4))
#
# #  Анонимные функции (Lambda-выражения)
#
#
# print((lambda x, y: x + y)(1, 2))
#
# fn = lambda x, y: x + y
# print(fn(5, 6))

# print((lambda x, y: x ** 2 + y ** 2)(2, 5))


# print((lambda a, b, c: a + b + c)(1, 2, 3))
# print((lambda a, b, c=3: a + b + c)(1, 2))
# print((lambda a, b, c=3: a + b + c)(b=1, a=2))
#
# print((lambda *args: sum(args))(1, 2, 3, 4, 5, 6))
# print((lambda *kwargs: sum(kwargs))(1, 2, 3, 4, 5, 6))


# c = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4,
# )
#
# for t in c:
#     print(t("abc__"))

#
# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# f = outer(5)
# print(f(10))
#
#
# def outer(n):
#     return lambda x: n + x
#
#
# f = outer(5)
# print(f(10))
#
# outer = lambda n: lambda x: n + x
#
# f = outer(5)
# print(f(10))
#
# print((lambda n: lambda x: n + x)(5)(10))


# def sort_list(i):
#     return i[1]
#
#
# d = {"b": 3, "c": 1, "a": 2}
# print(d)
# lst = list(d.items())
# print(lst)
# # lst.sort(key=lambda i: i[1])
# lst.sort(key=sort_list)
# print(lst)
# print(dict(lst))

#
# players = [
#     {"name": "Антон", "last name": "Бирюков", "rating": 9},
#     {"name": "Алексей", "last name": "Бодня", "rating": 10},
#     {"name": "Федор", "last name": "Сидоров", "rating": 4},
#     {"name": "Михаил", "last name": "Семенов", "rating": 6}
# ]
#
# print(sorted(players, key=lambda item: item["last name"]))
# print(sorted(players, key=lambda item: item["rating"], reverse=True))
# print(sorted(players, key=lambda item: item["rating"]))


# lst = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
#
#
# print(lst[0](10, 5))


# d = {
#     1: lambda: print("Понедельник"),
#     2: lambda: print("Вторник"),
#     3: lambda: print("Среда"),
#     4: lambda: print("Четверг"),
#     5: lambda: print("Пятница"),
#     6: lambda: print("Суббота"),
#     7: lambda: print("Воскресенье")
# }
#
# d[7]()

# print((lambda a, b: a if a > b else b)(15, 7))


#  map(func, *iterable), filter(func, *iterable)

# def mult(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
#
# print(list(map(mult, lst)))
# print(list(map(lambda t: t * 2, lst)))

# t = (2.88, -1.75, 100.55)
# print(tuple(map(lambda x: int(x), t)))
# print(tuple(map(int, t)))


# st = ["a", "b", "c", "d", "e"]
# num = [1, 2, 3, 4, 5]
# val = [2.0, 5.4, 7.8, 9.4, 7.4]
# print(list(map(lambda x, y, z: (x, y, z), st, num, val)))
# # print(dict(map(lambda x, y: (x, y, z), st, num, val)))

# print(list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(1, 10)))))
#
# print(list(range(1, 10)))
# print(list(filter(lambda x: x % 2, range(1, 10))))
# print(list(map(lambda x: x ** 2, range(1, 10))))
#
# print([x ** 2 for x in range(1, 10) if x % 2])


# Декораторы

# def hello():
#     return "Hello, I am func 'hello'"
#
#
# def super_func(func):
#     print("Hello, I am func 'super_func'")
#     print(func())
#
#
# super_func(hello)


# def hello():
#     return "Hello, I am func 'hello'"
#
#
# test = hello
# print(type(test))
# print(test())


# def my_decorator(func):
#     def inner():
#         print("Код до вызова функции")
#         func()
#         print("Код после вызова функции")
#     return inner
#
#
# def func_test():
#     print("Hello, I am func 'func_test'")


# test = my_decorator(func_test)
# test()

#
# def my_decorator(func):  # декорирующая функция
#     def inner():
#         print("Код до вызова функции")
#         func()
#         print("Код после вызова функции")
#
#     return inner
#
#
# @my_decorator  # декоратор
# def func_test():  # декорируемая функция
#     print("Hello, I am func 'func_test'")
#
#
# @my_decorator
# def hello():
#     print("Hello, I am func 'hello'")
#
#
# func_test()
# print()
# hello()


# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# @bold
# @italic
# def hello():
#     return "text"
#
#
# print(hello())
#
# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print("Вызов функции:", count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# @cnt
# def world():
#     print("World")
#
#
# hello()
# hello()
# hello()
# world()
# world()
# hello()


# def outer(fn):
#     def wrap(arg1, arg2):
#         print("Данные:", arg1, arg2)
#         fn(arg1, arg2)
#
#     return wrap
#
#
# @outer
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# print_full_name("Ирина", "Ветрова")


def outer(fn):
    def wrap(*args, **kwargs):
        fn(*args, **kwargs)

    return wrap

    # @outer
    # def print_students(a, b, c, study="Pyrhon"):
    #     print(a, b, c, "изучают", study, "\n")
    #
    #
    # # print_students("Борис",  'Елизаветата", "Светлана" study="Javascript")
    # print_students("Владимир", "Екатерина", "Виктрпр")

    # def decor(args1, args2):
    #     def args_dec(fn):
    #         def wrap(x, y):
    #             print(args1, x, args2, y, "=", end=" ")
    #             fn(x, y)
    #
    #         return wrap
    #
    #     return args_dec
    #
    #
    # @decor("Сумма:", "+")
    # def summa(a, b):
    #     print(a + b)
    #
    #
    # @decor("Разность", "-")
    # def sub(a, b):
    #     print(a - b)
    #
    #
    # summa(5, 2)
    # sub(5, 2)

    # def multiply(arg):
    #     def outer(fn):
    #         def inner(*args, **kwargs):
    #             return arg * fn(*args, **kwargs)
    #
    #         return inner
    #
    #     return outer
    #
    #
    # @multiply(3)
    # def return_num(num):
    #     return num
    #
    #
    # print(return_num(5))

    # def typed(*args, **kwargs):
    #     def wrapper(fn):
    #         def wrap(*f_args, **f_kwargs):
    #             for i in range(len(args)):
    #                 if type(f_args[i]) is not args[i]:  # !=
    #                     raise TypeError("Некорректный тип данных")
    #
    #             for k in kwargs:
    #                 if type(f_kwargs[k]) != kwargs[k]:
    #                     raise TypeError("Некорректный тип данных для именованного параметра")
    #
    #             return fn(*f_args, **f_kwargs)
    #
    #         return wrap
    #
    #     return wrapper
    #
    #
    # @typed(int, int, int)
    # def typed_fn(x, y, z):
    #     return x * y * z
    #
    #
    # @typed(str, str, str)
    # def typed_fn2(x, y, z):
    #     return x + y + z
    #
    #
    # @typed(str, str, z=int)
    # def typed_fn3(x, y, z="Hello!"):
    #     return (x + y) * z
    #
    #
    # print(typed_fn(3, 4, 5))
    # # print(typed_fn(3, 4, "Hello"))
    # print(typed_fn2("Hello", "World", "!"))
    # print(typed_fn3("Hello", "World", z=5))
    # print(typed_fn3("Hello", "World", z="Python"))

    # print(bin(18))  # 0b10010   - двоичная система исчисления
    # print(oct(18))  # 0o22   - восьмеричная система исчисления
    # print(hex(18))  # 0x12   - шестнадцетиричная система исчисления
    #
    # print(0b10010)
    # print(0o22)
    # print(0X12)
    # print(0x12 + 0b10010 + 0o22 + 18)

    #
    # q = "Pyt"
    # w = "hon"
    # e = q + w
    # print(e)
    # print(e * -3)

    # s = "Hello"
    # print(s, id(s))
    # # print(s[1])
    # # print(s[1:3])
    # # print(s[-1])
    # # print('a' in s)
    # s = s + "!"
    # print(s, id(s))

    # print("Привет")
    # print(u"Привет")

    # print("C:\\folder\\file.py")
    # print(r"C:\folder\file.py")
    # print(r"C:\folder\\"[:-1])
    # print(r"C:\folder" + "\\")
    # print("C:\\folder\\")

    # print(b"a1b2c4")
    #
    #
    # name = "Дмитрий"
    # age = 25
    # print("Меня зовут ", name, ". Мне ", age, " лет.", sep="")
    # print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
    # print(f"Меня зовут {name}. Мне {age} лет")


# print("Вносим изменения в локальный репозиторий")

# print("Работа на новом устройстве")

import re

s = "Я ищу совпадения в 2025 году. \"И я их найду в 2 счё-та\". [6789]. H.ello_World."
# reg = "\\."
# reg = r"\."
# reg = r"[12][0-9][0-9][0-9]"
# reg = r"[А-яЁё]"
# reg = r"[A-Z\[a-z\].-]"
# reg = r"[^0-9]"
# reg = r"\d"
# reg = r"\D"
# reg = r"\s"
# reg = r"\S"
# reg = r"\w"
# reg = r"сов\B"
# reg = r"\w*"
# print(re.findall(reg, s))  # список, содержащий все совпадения
# print(re.search(reg, s))  # месторасположение первого совпадения с шаблоном
# # print(re.search(reg, s).span())
# # print(re.search(reg, s).start())
# # print(re.search(reg, s).end())
# # print(re.search(reg, s).group())
# print(re.match(reg, s))  # месторасположение первого совпадения с шаблоном в начале строки
# print(re.split(reg, s))  # возвращает список, в котором строка разбита по шаблону.
# print(re.sub(reg, "!", s, 1))  # возвращает список, в котором строка разбита по шаблону.
# reg = r"\w*"
# reg = r"^\w+\s\w+"
# reg = r"\w+\.$"
reg = r"я"


# print(re.findall(reg, s, re.IGNORECASE))

# st = "Час в 24-часовом формате от 00 до 23. 2021-06-15T21:45. Минуты, в диапазоне от 00 до 59. 2021-06-15T01:09."
# reg1 = "[0-2][0-9]:[0-5][0-9]"
# print(re.findall(reg1, st))

# d = "Цифры: 7б, +17, --42, 0013, 0.3345.3890"
# # print(re.findall(r"[-+]?\d+\.?\d*", d))
# print(re.findall(r"[+-]?\d+[.\d]*", d))

# d = "05-03-1987 # Дата рождения"
#
# print("Дата рождения: ", re.sub(r"\s#.*", "", d))
# print("Дата рождения: ", re.sub(r"-", ".", d))
# print("Дата рождения: ", re.sub(r"-", ".", re.sub(r"-", ".", d)))
# # print("Дата рождения: ", "05.03.1987"))

# st = "author=Пушкин А. С.; title = Евгений Онегин; price =200; year= 1831"
# # reg1 = r"\w+\s*=\s*\w+\s*[\s\w.]*"
# reg1 = r"\w+\s*=[^;]*"
# print(re.findall(reg1, st))
# print(re.split(r";\s+", st))

# s1 = "12 сентября 2025 года 456543131"
# # reg1 = r"\d{4}"
# reg1 = r"\d{2,4}"
# # reg1 = r"\d{,4}"
# # reg1 = r"\d{2,}"
# print(re.findall(reg1, s1))

# st = "+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578"
# reg1 = r"\+?7\d{10}"
# print(re.findall(reg1, st))
#
# def validate_login(login):
#     return re.findall(r"^[A-za-z0-9_-]{3,16}$", login)
#
#
# print(validate_login("maasdss"))

# print(re.findall(r"\w+", "12 + й"))
# print(re.findall(r"\w+", "12 + й", flags=re.ASCII))

# text = "hello world"
# print(re.findall(r"\w\+", text, flags=re.DEBUG))


# text = """
# one
# two
# """
# # print(re.findall(r"one.\w+", text))
# # print(re.findall(r"one.\w+", text, re.DOTALL))
#
# print(re.findall(r"one$", text))
# print(re.findall(r"one$", text, re.MULTILINE))


# print(re.findall("""
# [a-z._-]+   # part1
# @           # @
# [a-z.-]+    # part2
# """, "test@mail.ru", re.VERBOSE))

# text = """Python,
# python,
# PYTHON"""
# reg1 = "(?mi)^python"
# print(re.findall(reg1, text))

# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall("<.*?>", text))

#  *?, +?, ??
# {m,n}?, {,n}?, {m,}?

# s1 = "12 сентября 2025 года 456543131"
# # reg1 = r"\d{4}"
# # reg1 = r"\d{2,4}?"
# # reg1 = r"\d{,4}"
# reg1 = r"\d{2,}"
# print(re.findall(reg1, s1))

