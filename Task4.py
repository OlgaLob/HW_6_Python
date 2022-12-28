# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 
# 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

from functools import reduce
a = list(map(int, input('Введите две координаты первой точки A, через пробел: ').split())) 
b = list(map(int, input('Введите две координаты второй точки B, через пробел: ').split()))
def a_b_distance(a, b):
     distance = reduce(lambda x, y: (x + y)**(1/2), (map(lambda a_b: (a_b[1] - a_b[0])**2, zip(a, b))))
     return round(distance, 2)
print(a_b_distance(a, b))