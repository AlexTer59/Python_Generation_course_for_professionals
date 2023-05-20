import time
from math import factorial                   # функция из модуля math
#start_time = time.perf_counter()
#a = factorial(900)
#end_time = time.perf_counter()
#print(end_time - start_time)

#def factorial_recurrent(n):
    #if n == 0:
        #return 1
    #return n * factorial_recurrent(n - 1)


def factorial_classic(n):                    # итеративная функция
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


start_time = time.perf_counter()
factorial_classic(900)
end_time = time.perf_counter()
print(end_time - start_time)