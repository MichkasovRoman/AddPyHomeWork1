# Задача 102 Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

import os
os.system('cls')

def GetListOfDiv(n):
    listDiv = []
    i = 1
    while i <= abs(n):
        if n % i == 0:
            listDiv.append(i)
        i = i + 1
    return listDiv

number = int(input('Введите целое число: '))
if number == 0:
    print('Некорректный ввод данных: ')
else:
    listSimple = []
    for el in GetListOfDiv(number):
        if len(GetListOfDiv(el)) == 2:
            listSimple.append(el)
    print(f'Список простых множителей числа {number}: {listSimple}')

