"""
Программа, которая считает стоимость трёх компьютеров, состоящих из монитора, системного блока, клавиатуры и мыши.
"""

"""
Пример ввода 1:
9900
55600
3999
2990

Пример вывода 1:
217467
---------------
Пример ввода 2:
15700
80550
12050
5890

Пример вывода 2:
342570
---------------
Пример ввода 3:
44990
123300
19600
8990

Пример вывода 3:
590640
"""

# Решение
monitor, system_unit, keyboard, mouse = int(input()), int(input()), int(input()), int(input())
print(3 * (monitor + system_unit + keyboard + mouse))