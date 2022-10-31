# Задайте последовательность чисел. Напишите программу 
# которая выведет список неповторяющихся элементов 
# исходной последовательности.

from ast import comprehension


# list1 = [1, 2, 2, 3, 3, 3, 4, 4, 5, 6, 7, ]
# list2 = []
# for i in range(len(list1) - 1):
#     if list1.count(i) == 1:
#         list2.append(i)
# print(list2)        
# ЧЕРЕЗ LIST comprehension
lst = [1, 3, 5, 6, 9, 0, 3, 5, 7, 9, 56]
lst1 = [i for i in lst if lst.count(i) == 1]
print(f'Исходный список: {lst}')
print(f'Список неповторяющихся элементов: {lst1}')
lst2 = list(set(lst))
print(f'Список уникальных элементов через множество: {lst2}')
lst3 = list()
for i in lst:
    if i not in lst3:
        lst3.append(i)
print(f'Список уникальных элементов: {lst3}')
lst4 = [lst[i] for i in range(len(lst)) if lst[0: i].count(lst[i]) == 0]
print(f'Список уникальных элементов через генератор: {lst4}')        
