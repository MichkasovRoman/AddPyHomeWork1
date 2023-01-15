# Задача 103 Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл file1.txt многочлен степени k.

# Пример:  k=2 

# Возможные варианты многочленов:
# 2*x*x + 4*x + 5 = 0 
# x*x + 5 = 0 
# 10*x*x = 0

import os
os.system('cls')

def Xdegree(n):
    degree = 'x'
    i = 0
    while i < n - 1:
        degree = degree + '*x'
        i = i + 1
    return degree

def IfNullCoef(n, m):
    if n == 0:
        return ''
    elif n == 1:
        return ' ' + '+' + ' ' + Xdegree(m)
    else:
        return ' ' + '+' + ' ' + str(n) + '*' + Xdegree(m)

k = int(input('Введите степень многочлена: '))
txt = f'Degree {k} polynomial: f(x) = '
import random      
coefficients = []
for coef in range(0, k + 1):
    coefficients.append(random.randint(0, 100))
print(f'List of coefficients of a degree {k} polynomial: {coefficients}')

if coefficients[0] == 0:
    print('Первый коэффициент не может равняться нулю. Перезапустите код.')
else:
    polynomial = IfNullCoef(coefficients[0], k).replace(' ' + '+' + ' ', '')
    i = 1
    while i < k:
        polynomial = polynomial + IfNullCoef(coefficients[i], k - i)
        i = i + 1
    
    if coefficients[k] == 0:
        print(txt + polynomial)
    else:
        print(txt + polynomial + ' ' + '+' + ' ' + str(coefficients[k]))

    data = open('file1.txt', 'w')
    data.writelines(txt + polynomial + ' ' + '+' + ' ' + str(coefficients[k]))
    data.close()
