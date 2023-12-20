import math


def cg_distance(x1, y1, x2, y2, x3, y3, x4, y4) -> float:  #центры
    Ax = (x1 + x2) / 2
    Ay = (y1 + y2) / 2
    Bx = (x3 + x4) / 2
    By = (y3 + y4) / 2
    AB = math.sqrt((Ax - Bx) ** 2 + (Ay - By) ** 2)
    return round(AB, 2)


def corner_distance(x1, y1, x2, y2, x3, y3, x4, y4) -> float:  #углы
    left = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
    right = math.sqrt((x4 - x2) ** 2 + (y4 - y2) ** 2)
    AB = left + right
    return round(AB, 2)


while True:
    menu = input("центр/углы/выход")
    x1, y1 = map(int, input("Введите координаты левого угла первого прямоугольника через пробел").split(' '))
    x2, y2 = map(int, input("Введите координаты правого угла первого прямоугольника через пробел").split(' '))
    x3, y3 = map(int, input("Введите координаты левого угла второго прямоугольника через пробел").split(' '))
    x4, y4 = map(int, input("Введите координаты правого угла второго прямоугольника через пробел").split(' '))
    if menu == "выход":
        break
    if menu == "центр":
        print("Расстояние между центрами тяжести прямоугольников:")
        print(cg_distance(x1, y1, x2, y2, x3, y3, x4, y4))

    if menu == "углы":
        print("Сумма расстояний между углами прямоугольников:")
        print(corner_distance(x1, y1, x2, y2, x3, y3, x4, y4))

