"""
Программа, которая определяет, может ли конь попасть с первой клетки на вторую одним ходом. Программа получает на вход
четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.
Программа должна вывести «YES», если из первой клетки ходом коня можно попасть во вторую, или «NO» в противном случае.
"""

"""
Пример ввода:
1
1
2
2

Пример вывода:
YES
"""

# Решение
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if x1 == x2 or y1 == y2 or x1 - y1 == x2 - y2 or x1 + y1 == x2 + y2:
    print("YES")
else:
    print("NO")
