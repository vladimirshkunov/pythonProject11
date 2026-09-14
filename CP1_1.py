"""
Задача 1. Заданы длины трех отрезков. Определиить, какой трекгольник из них получится
(разносторонний, равнобедренный, равносторонний) или не получится совсем.
"""
a, b, c = map(int, input().split())
if a + b <= c or a + c <= b or c + b <= a:
    print("No triangle")
elif a == b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
