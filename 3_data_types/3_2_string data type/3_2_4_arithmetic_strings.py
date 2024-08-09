"""
Программа, которая выясняет, можно ли из длин трех строк построить арифметическую прогрессию.
"""

"""
Пример ввода 1:
abc
a
abcde

Пример вывода 1:
YES
---------------
Пример ввода 2:
2434
90099
21

Пример вывода 2:
NO
---------------
Пример ввода 3:
aaaaaaaaaa10
1111111Nm
22222r

Пример вывода 3:
YES
"""

# Решение
len_1, len_2, len_3 = len(input()), len(input()), len(input())

min_len = min(len_1, len_2, len_3)
max_len = max(len_1, len_2, len_3)

if (min_len + max_len) / 2 == len_1 or (min_len + max_len) / 2 == len_2 or (min_len + max_len) / 2 == len_3:
    print("YES")
else:
    print("NO")
