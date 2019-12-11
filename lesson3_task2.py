# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив
# надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля), т.к.
# именно в этих позициях первого массива стоят четные числа.

import random

my_list = []
NUM = 10

for _ in range(NUM):
    my_list.append(random.randint(0, 100))

resault = []

for i, el in enumerate(my_list):
    if el % 2 == 0:
        resault.append(i)

print(my_list)
print(resault)