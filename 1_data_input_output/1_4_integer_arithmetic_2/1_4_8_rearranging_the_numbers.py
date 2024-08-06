"""
Программа, которая выводит шесть чисел, образованных при перестановке цифр заданного трехзначного числа.
"""

"""
Пример ввода 1:
123

Пример вывода 1:
123
132
213
231
312
321
---------------
Пример ввода 2:
987

Пример вывода 2:
987
978
897
879
798
789
"""

# Решение
num = int(input())

first_digit = num // 100
second_digit = num // 10 % 10
third_digit = num % 10

print(str(first_digit), str(second_digit), str(third_digit), sep="")
print(str(first_digit), str(third_digit), str(second_digit), sep="")
print(str(second_digit), str(first_digit), str(third_digit), sep="")
print(str(second_digit), str(third_digit), str(first_digit), sep="")
print(str(third_digit), str(first_digit), str(second_digit), sep="")
print(str(third_digit), str(second_digit), str(first_digit), sep="")
