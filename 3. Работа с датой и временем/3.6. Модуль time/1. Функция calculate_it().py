import time
start_time = time.perf_counter()
def calculate_it(func, *args):
    return func(*args), time.perf_counter() - start_time

def add(a, b, c):
    time.sleep(3)
    return a + b + c

print(calculate_it(add, 1, 2, 3))