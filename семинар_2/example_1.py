"""
Циклы for и while + else
Вывод через принт с командой end
"""

for i in range(0, 5, 2):
    print(i)

stroka = "qwerty"
for el in stroka:
    print(el)

i = 0
while (i < 5):
    n = int(input("Ввод: "))
    if n == 0:
        break
    i += 1
else:
    print("Конец")

stroka = "qwerty"
for el in stroka:
    print(el, end=" ")  # end дает возможность выбрать конкретное окончание предъидущего принта
print("qqqq")
print("qqqq")
