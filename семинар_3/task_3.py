"""
Напишите программу для печати всех уникальных значений в словаре. {"V": "S001", "V": "S002", "VI": "S001",
"VI": "S005", "VII": " S005 ", " V ":" S009 ", " VIII ":" S007 ", "IV":"holla", "1234": "S005"}

"""

slovar_1 = {"V": "S002", "VI": "S005", "VII": " S005 ", " V ": " S009 ", " VIII ": " S007 ", "IV": "holla", "1234": "S005"}

list_1 = []
for i in slovar_1:
    if slovar_1[i] not in list_1:
        list_1.append(slovar_1[i])
print(list_1)

""""
test_list = {"V": "S001", "V": "S002", "VI": "S001", "VI": "S005", "VII": " S005 ", " V ":" S009 ", " VIII ":" S007 ", "IV":"holla", "1234": "S005"}
#res = list(set(val for dic in test_list for val in dic.values()))
a = set()

for value in test_list.values():
     a.add(value)

print(sorted(a))
"""