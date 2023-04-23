"""
Посчитать факториал (произведение 1 до N) и треугольное число (сумма чисел от 1 до N)
для числа N ЧЕРЕЗ РЕКУРСИЮ и без циклов
"""


def fac(n):
    if n == 1:
        return 1
    return fac(n - 1) * n

def summ(n):
    return sum(range(n+1))

number = int(input("Enter your number "))

print("Factorial: ", + fac(number))
print("Triangular: ", + summ(number))
