# Определить, какое число в массиве встречается чаще всего.

import random

my_list = []
count_list = []
nums_list = []

for _ in range(10):
    my_list.append(random.randint(0, 100))

for el in my_list:
    fl = False
    for i, el_num in enumerate(nums_list):
        if el_num == el:
            fl = True
            count_list[i]+=1
            break
    if not fl:
        nums_list.append(el)
        count_list.append(1)

print(my_list)
print(nums_list)
print(count_list)
