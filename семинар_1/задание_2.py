"""
2) 3. В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами.
За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов.
Выведите наименьшее число парт, которое нужно приобрести для них.

**Input:**

20

21

22

**Output:**

32
"""

print("Введите количество учеников")
n1 = int(input("Введите количество учеников в 1ом классе : "))
n2 = int(input("Введите количество учеников в 2ом классе : "))
n3 = int(input("Введите количество учеников в 3ом классе : "))

c = int((n1 / 2) + 0.5) + int((n2 / 2) + 0.5) + int((n3 / 2) + 0.5)
print(f"Понадобится {c} парт")
