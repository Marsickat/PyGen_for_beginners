"""
Программа, которая находит пересечение двух отрезков.
"""

"""
Пример ввода 1:
1
3
2
4

Пример вывода 1:
2 3
---------------
Пример ввода 2:
1
2
3
441

Пример вывода 2:
пустое множество
----------------
Пример ввода 3:
5
6
6
80

Пример вывода 3:
6
"""

# Решение
a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())

if a1 <= a2 <= b1 <= b2:
    if a2 == b1:
        print(a2)
    else:
        print(a2, b1)
elif a2 <= a1 <= b2 <= b1:
    if a1 == b2:
        print(a1)
    else:
        print(a1, b2)
elif a1 <= a2 <= b2 <= b1:
    print(a2, b2)
elif a2 <= a1 <= b1 <= b2:
    print(a1, b1)
else:
    print("пустое множество")