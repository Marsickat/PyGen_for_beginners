"""
Программа, которая определяет номер купе, где находится место с заданным номером (нумерация мест сквозная, начинается с
1).

В купейном вагоне имеется 9 купе с четырьмя местами для пассажиров в каждом.
"""

"""
Пример ввода 1:
1

Пример вывода 1:
1
---------------
Пример ввода 2:
6

Пример вывода 2:
2
---------------
Пример ввода 3:
19

Пример вывода 3:
5
"""

# Решение
compartment = int(input())
print((compartment - 1) // 4 + 1)
