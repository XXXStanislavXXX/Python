"""
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
"""

def rec_summ(a, b):
    if a == 0:
        return b
    else:
        return rec_summ(a - 1, b + 1)

num_1 = int(input("Enter 1st number "))
num_2 = int(input("Enter 2nd number "))

print(rec_summ(num_1, num_2))
