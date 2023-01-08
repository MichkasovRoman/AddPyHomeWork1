# Задача 101 Вычислить число π c заданной точностью d

# Пример: 
# при d = 0.001, π = 3.141    0.1 ≤ d ≤ 0.00000000001

import os
os.system('cls')

d = input('Введите точность: ')
l = len(d)
if float(d) * (10 ** (l - 2)) == 1 and 0.00000000001 <= float(d) <= 0.1:
    import math
    print('Число π = ', math.pi)
    piString = str(math.pi)
    
    i = 0
    piWithout = ''
    while i < l - 1:
        piWithout = piWithout + piString[i]
        i = i + 1
    
    m = int(piString[l])
    n = int(piString[l - 1])
    if 5 <= m <= 9:
        piRound = piWithout + str(n + 1)
    else:
        piRound = piWithout + str(n) 
    print(f'Его округленное значение с точностью до {d} равно {float(piRound)}')
else:
    print('Некорректный формат ввода.')