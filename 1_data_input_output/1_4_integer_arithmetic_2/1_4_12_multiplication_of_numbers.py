"""
Программа, которая считывает целое положительное число n и выводит значение числа n + nn + nnn.
"""

"""
Пример ввода 1:
1

Пример вывода 1:
123
---------------
Пример ввода 2:
2

Пример вывода 2:
246
---------------
Пример ввода 3:
3

Пример вывода 3:
369
---------------
Пример ввода 4:
9

Пример вывода 4:
1107
"""

# Решение
n = int(input())
n2 = n * 11
n3 = n * 111
print(n + n2 + n3)