import random

# task 4

# Написать программу, которая генерирует в указанных пользователем границах:
# ● случайное целое число, ● случайное вещественное число, ● случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

a = 1
b = 10
print(random.randint(a, b))

a = -10
b = 10
print(random.randint(a, b))

a = 'f'
b = 'r'
a.encode('windows-1251')
b.encode('windows-1251')
print(chr(random.randint(ord(a), ord(b))))