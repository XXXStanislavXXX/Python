"""
Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n
(включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k.
Программа получает на вход одно натуральное число k, не превосходящее 10^5.
Программа должна вывести все пары дружественных чисел, каждое из которых не превосходит k.
Пары необходимо выводить по одной в строке, разделяя пробелами.
Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).

Делители n == m И делители m == n
"""


def deliteli(num):
    count = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            count += i + num//i
    return count


k = int(input("Kakni "))

for i in range(k - 1):
    j = deliteli(i)
    if deliteli(j) == i & i > j:
        print(j, i)
