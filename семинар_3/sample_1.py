"""
Пример работы со словарем
"""

slovar = {"1": "one", "2": "one"}
print(slovar)
slovar["privet"] = "one"
print(slovar)
# for item in slovar:
#     print(item, slovar[item])
spisok = []
for key, value in slovar.items():
    spisok.append([key, value])

print(spisok)

spisok = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(spisok[5:2:-1])

spisok2 = spisok[::-1]
print(spisok2)