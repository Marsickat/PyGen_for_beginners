"""
Программа, которая находит серединное значение из трех различных чисел.
"""

"""
Пример ввода 1:
1
2
3

Пример вывода 1:
2
---------------
Пример ввода 2:
10
30
20

Пример вывода 2:
20
"""

# Решение
num1, num2, num3 = int(input()), int(input()), int(input())

if num1 < num2 < num3 or num3 < num2 < num1:
    print(num2)
elif num1 < num3 < num2 or num2 < num3 < num1:
    print(num3)
elif num2 < num1 < num3 or num3 < num1 < num2:
    print(num1)
