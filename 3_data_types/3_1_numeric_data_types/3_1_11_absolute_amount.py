"""
Программа, которая вычисляет сумму модулей пяти чисел
"""

"""
Пример ввода 1:
5.4
33
-1232
-3.889
6

Пример вывода 1:
1280.289
---------------
Пример ввода 2:
0
-776.4
0
343
55.24

Пример вывода 2:
1174.64
---------------
Пример ввода 3:
-5.4643234
0
223
5
7

Пример вывода 3:
240.4643234
"""

# Решение
a1, a2, a3, a4, a5 = float(input()), float(input()), float(input()), float(input()), float(input())

print(abs(a1) + abs(a2) + abs(a3) + abs(a4) + abs(a5))
