import timeit
import cProfile

s = """
s = 123
output__sum = 0
output__mul = 1
s1 = s
output__sum = output__sum + s1 % 10
s1 = s1 // 10
output__sum = output__sum + s1 % 10
s1 = s1 // 10
output__sum = output__sum + s1
print('sum=', output__sum)

output__mul = output__mul * s % 10
s = s // 10
output__mul = output__mul * s % 10
s = s // 10
output__mul = output__mul * s
print('mul=', output__mul)
"""

print(timeit.timeit(s, number=100))
# 0.002474172
cProfile.run(s)
"""
5 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:2(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}"""