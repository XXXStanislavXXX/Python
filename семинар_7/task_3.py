"""
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр

123  --> 6
1.23 --> 6

"""

digit = input("enter number ")

print(digit)

digit = digit.replace(".", "").replace(",", "")

print(digit)

result_1 = sum(map(int, digit))

print(result_1)

