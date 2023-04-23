"""
Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит число
А в целую степень B с помощью рекурсии.
"""
def degree (a, b, c):
    if b != 0:
        c *= a
        b -= 1
    else:
        return c
    return degree(a, b, c)

num1 = int(input("Введи число А: "))

num2 = int(input("Введи число Б: "))

c = 1

print(degree(num1, num2, c))
