# Задача 1
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

'''
import random

n = int(input('Введите количество монет: '))

heads = 0
tails = 0

for i in range(n):
    coin = random.randint(0, 1)
    if coin == 0:
        tails += 1
    elif coin == 1:
        heads += 1    
    print(coin, end=' ')
print('- выпали такие монеты')

min_flips = min(heads, tails)
print('Минимальное количество монет, которые нужно перевернуть:', min_flips)
'''

'''
# Задача 2
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

import random
x = int(random.randint(1, 1000))
y = int(random.randint(1, 1000))

s = x + y
p = x * y

print('сумма загаданных чисел -', s)
print('произведение загаданных чисел -', p)

for x in range(1, 1001):
    for y in range(1, 1001):
        s2 = x + y
        p2 = x * y
        if s == s2 and p == p2:
            print(f'Загаданные числа: {x} и {y}')
            exit()
'''

'''
# Задача 3
# Требуется вывести все целые степени двойки 
# (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

n = int(input("Введите число N: "))
k = 0
while 2**k <= n:
    print(2**k, end=' ')
    k += 1
'''