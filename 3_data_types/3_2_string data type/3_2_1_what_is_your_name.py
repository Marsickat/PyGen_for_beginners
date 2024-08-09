"""
Программа, которая считывает с клавиатуры две строки – имя и фамилию пользователя и выводит фразу:

Hello <введённое имя> <введённая фамилия>! You have just delved into Python
"""

"""
Пример ввода 1:
Anthony
Joshua

Пример вывода 1:
Hello Anthony Joshua! You have just delved into Python
------------------------------------------------------
Пример ввода 2:
Michael
Jordan

Пример вывода 2:
Hello Michael Jordan! You have just delved into Python
------------------------------------------------------
Пример ввода 3:
Leonardo
DiCaprio

Пример вывода 3:
Hello Leonardo DiCaprio! You have just delved into Python
"""

# Решение
name, surname = input(), input()

print("Hello", name, surname + "!", "You have just delved into Python")
