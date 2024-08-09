"""
Программа, которая определяет самое короткое и самое длинное название из трех городов.
"""

"""
Пример ввода 1:
Москва
Санкт-Петербург
Екатеринбург

Пример вывода 1:
Москва
Санкт-Петербург
---------------
Пример ввода 2:
Нью-Йорк
Вашингтон
Чикаго

Пример вывода 2:
Чикаго
Вашингтон
---------------
Пример ввода 3:
Париж
Марсель
Лион

Пример вывода 3:
Лион
Марсель
"""

# Решение
city_1, city_2, city_3 = input(), input(), input()

len_city_1, len_city_2, len_city_3 = len(city_1), len(city_2), len(city_3)

if len_city_1 < len_city_2 < len_city_3:
    print(city_1, city_3, sep="\n")
elif len_city_1 < len_city_3 < len_city_2:
    print(city_1, city_2, sep="\n")
elif len_city_2 < len_city_1 < len_city_3:
    print(city_2, city_3, sep="\n")
elif len_city_2 < len_city_3 < len_city_1:
    print(city_2, city_1, sep="\n")
elif len_city_3 < len_city_1 < len_city_2:
    print(city_3, city_2, sep="\n")
elif len_city_3 < len_city_2 < len_city_1:
    print(city_3, city_1, sep="\n")
