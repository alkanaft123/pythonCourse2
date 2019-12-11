# В одномерном массиве найти сумму элементов,
# находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

my_list = []

for _ in range(10):
    my_list.append(random.randint(0, 100))
print('list:', my_list)

max = float('-inf')
max_ind = float('-inf')
min = float('inf')
min_ind = float('inf')

for i, el in enumerate(my_list):
    if el > max:
        max = el
        max_ind = i
    if el < min:
        min = el
        min_ind = i
print('min:', min, ', min index:', min_ind, ', max:', max, ', max index:', max_ind)

my_sum = 0
for el in my_list[min_ind + 1 if min_ind < max_ind else max_ind + 1: max_ind if max_ind > min_ind else min_ind]:
    my_sum+=el
print('sum = ', my_sum)