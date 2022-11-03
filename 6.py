# Задайте последовательность чисел. Напишите программу 
# которая выведет список неповторяющихся элементов 
# исходной последовательности.

# from ast import comprehension


# list1 = [1, 2, 2, 3, 3, 3, 4, 4, 5, 6, 7, ]
# list2 = []
# for i in range(len(list1) - 1):
#     if list1.count(i) == 1:
#         list2.append(i)
# print(list2)        
# ЧЕРЕЗ LIST comprehension
# lst = [1, 3, 5, 6, 9, 0, 3, 5, 7, 9, 56]
# lst1 = [i for i in lst if lst.count(i) == 1]
# print(f'Исходный список: {lst}')
# print(f'Список неповторяющихся элементов: {lst1}')
# lst2 = list(set(lst))
# print(f'Список уникальных элементов через множество: {lst2}')
# lst3 = list()
# for i in lst:
#     if i not in lst3:
#         lst3.append(i)
# print(f'Список уникальных элементов: {lst3}')
# lst4 = [lst[i] for i in range(len(lst)) if lst[0: i].count(lst[i]) == 0]
# print(f'Список уникальных элементов через генератор: {lst4}')        

# st = 'My name is Evgeniy'
# lst = st.split()# разделение сплитом 
# print(lst) 

# import re
# from unittest import result

# a = 'Beautiful, is; better*than\nugly'
# result = re.split('; |, |\*|\n', a)# функция сплит из библиотеки re
# print(result)

# a = eval('1+3+4')# небезопасная функция
# print(a)

# import numexpr as ne # почему не добавляется библиотека?
# a = ne.evaluate('1/3+2/3')
# print(a)

#5+10
# from unittest import result


# st = '5+10'
# if '+' in st:
#     index = st.find('+')
#     a = float(st[: index]) # нарезка строки
#     b = float(st[index + 1:])
#     result = a + b
# elif '-' in st:
#     a = 1
#     b = 1
#     result = a - b
# print(result)        



Домашнее задание
1
Задайте список из нескольких чисел. 
Напишите программу, которая найдёт сумму элементов списка, 
стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

n = int(input('Количество элементов списка: '))
b1 = int(input('Граница 1 диапазона значений элементов списка: '))
b2 = int(input('Граница 2 диапазона значений элементов списка: '))
lst = [random.randint(min(b1, b2), max(b1, b2)) for i in range(n)]
sum_odd = sum(lst[item] for item in range(1, len(lst), 2))
odd_el = str([lst[item] for item in range(1, len(lst), 2)]).strip('[]')
print(f'Для списка {lst} сумма чисел, стоящих на нечётных позициях: \n{odd_el} равна {sum_odd}.')


2
Напишите программу, которая найдёт произведение пар чисел списка. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]

from random import randint
number = int(input('Введите размер списка '))
list = [randint(0, 9) for i in range(number)] 
list2 = []
#for i in range(number):
#list.append(randint(0, 9))
for i in range(len(list)):
    while i < len(list)/2 and number > len(list)/2:
        number = number - 1
        a = list[i] * list[number]
        list2.append(a)
        i += 1

print(list)
print(list2)