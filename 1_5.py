#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.


print("Введите координаты точки А")
pointA = [int(input()), int(input())]
print("Введите координаты точки В")
pointB = [int(input()), int(input())]

lengthSegment = ((pointB[0] - pointA[0]) ** 2 + (pointB[1] - pointA[1]) ** 2) ** (0.5)
print(f"Длина отрезка: {format(lengthSegment, '.2f')}")