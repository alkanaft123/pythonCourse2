# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

my_list = []

for _ in range(10):
    my_list.append(random.randint(0, 100))


print(my_list)

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


my_list[min_ind], my_list[max_ind] = my_list[max_ind], my_list[min_ind]
print(my_list)
