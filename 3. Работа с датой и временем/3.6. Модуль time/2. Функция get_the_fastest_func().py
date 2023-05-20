import time
def get_the_fastest_func(funcs, arg):
    times = []
    for i in funcs:
        start_time = time.perf_counter()
        i(arg)
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    return funcs[times.index(min(times))]

def the_first(arg):
    time.sleep(1)
    return arg, 'first'

def the_second(arg):
    time.sleep(0)
    return arg, 'second'

string = 'hi'
print(get_the_fastest_func([the_first, the_second], string))
