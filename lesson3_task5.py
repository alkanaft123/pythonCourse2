# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве. Примечание
# к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.

import random

my_list = []

for _ in range(10):
    my_list.append(random.randint(-100, 100))

max = float('-inf')
max_ind = float('-inf')

for i,el in enumerate(my_list):
    if el < 0:
        if el > max:
            max = el
            max_ind = i

print(my_list)
print('el: ', max, ' index: ', max_ind)

