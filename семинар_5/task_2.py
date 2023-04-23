"""
Дано натуральное чисел N и последовательность из N элементов.
Требуется вывести эту последовательность в обратном порядке.
"""

def rotate (n):
    if n == 0:
        return " "
    else:
        a = int(input("Value "))
        return rotate(n-1) + f"{a} "


n = int(input("Enter n: "))

print(rotate(n))
