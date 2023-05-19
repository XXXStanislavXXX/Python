"""
Дан список, вывести отдельно буквы и цифры, пользуясь filter.

[12,'sadf',5643] ---> ['sadf'] ,[12, 5643]

"""

list_2 = [12, 'sadf', 5643]

result_list_2 = list(filter(lambda x: type(x) == int, list_2))
result_list_3 = list(filter(lambda x: type(x) != int, list_2))

print(result_list_2, result_list_3)

