import timeit
import cProfile
n = 100
# example 1
s = """
n = 100
lst = []
k = 0
for i in range(2, n+1):
    for j in range(2, i):
        if i % j == 0:
            k = k + 1
    if k == 0:
        lst.append(i)
    else:
        k = 0
# print(lst)
"""
print(timeit.timeit(s, number=100))
# 0.03912359099999999
cProfile.run(s)
"""
  28 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:2(<module>)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
       25    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""


# example 2
s = """
n = 100
lst=[2]
for i in range(3, n+1, 2):
	if (i > 10) and (i%10==5):
		continue
	for j in lst:
		if j*j-1 > i:
			lst.append(i)
			break
		if (i % j == 0):
			break
	else:
		lst.append(i)
# print(lst)
"""
print(timeit.timeit(s, number=100))
# 0.002354579999999995
cProfile.run(s)
"""
   27 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:2(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       24    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}"""