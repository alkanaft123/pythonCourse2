## 7. Напишите программу, доказывающую или проверяющую, что для множества
# натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число.

def calculate(sum, i, n):
    if i == n:
        return sum + i
    else:
        return calculate(sum + i, i + 1, n)

n = input('enter N')
if n.isdigit():
    n = int(n)
    sum = calculate(0, 1, n)
    sum2 = n * (n + 1) / 2
    if sum == sum2:
        print(sum, sum2, True)
    else:
        print(sum, sum2, False)

