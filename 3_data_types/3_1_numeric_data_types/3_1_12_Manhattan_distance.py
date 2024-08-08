"""
Программа, определяющую манхэттенское расстояние между двумя точками, координаты которых заданы.

На плоскости манхэттенское расстояние между двумя точками (p₁; p₂) и (q₁; q₂) определяется так: |p₁ - q₁| + |p₂ - q₂|
"""

"""
Пример ввода:
10
15
21
13

Пример вывода:
13
"""

# Решение
p1, p2, q1, q2 = int(input()), int(input()), int(input()), int(input())

print(abs(p1 - q1) + abs(p2 - q2))