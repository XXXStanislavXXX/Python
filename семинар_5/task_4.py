"""
Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.


1 5 2 1 5 4
"""

from random import randint

n1_set = list(randint(1, 5) for i in range(int(input('Введите кол-во элементов первого множества: '))))
print(n1_set)


def change(list_1):
    min_num = min(list_1)
    max_num = max(list_1)
    for i in range(len(list_1)):
        if list_1[i] == max_num:
            list_1[i] = min_num
    return list_1


print(change(n1_set))
