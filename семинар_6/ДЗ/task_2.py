"""
Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
"""

import random

max = int(input("Enter MAX "))
min = int(input("Enter MIN "))

a_1 = int(input("Enter mass legth "))

mass_1 = []
for el_2 in range(a_1):
    mass_1.append(random.randint(min, max))
print(mass_1)

list_2 = []
for i in range(len(mass_1)):
    if min <= mass_1[i] <= max:
        print(i, end=' ')
