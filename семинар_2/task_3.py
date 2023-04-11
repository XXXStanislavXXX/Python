"""
 Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача:
арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел,
записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза.
 Все числа натуральные и не превышают 30000.
"""

mellons = int(input("Введите количество арбузов "))
i = 0
min_w = 30000
max_w = 0
while i < mellons:
    mellon_weight = int(input("Введите вес арбуза "))
    if mellon_weight > max_w:
        max_w = mellon_weight
    if mellon_weight < min_w:
        min_w = mellon_weight
    i += 1
print(min_w, max_w)

"""
v2
Arbuz = int(input("Enter arbuz: "))
VesMin =VesMax= int(input("Ves Arbuz: "))
for i in range (1, Arbuz):
    temp = int(input("Ves Arbuz: "))
    if temp > VesMax:
        VesMax=temp
    elif temp < VesMin:
        VesMin=temp
print(f"Для тещи {VesMin}, Для себя {VesMax}")
"""