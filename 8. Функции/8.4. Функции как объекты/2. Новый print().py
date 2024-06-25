'''
Напишите программу, которая переопределяет встроенную функцию print() так, чтобы она печатала все переданные строковые
аргументы в верхнем регистре.

Примечание 1. Значения sep и end также должны переводиться в верхний регистр.

Примечание 2. В тестирующую систему сдайте программу, содержащую только переопределенную функцию print(), но не код,
вызывающий ее.
'''

old_print = print


def print(*args, **kwargs):
    caps = tuple(el.upper() if type(el) is str else el for el in args)
    if kwargs:
        kwargs['sep'] = kwargs['sep'].upper()
        kwargs['end'] = kwargs['end'].upper()
        return old_print(*caps, sep=kwargs['sep'], end=kwargs['end'])
    return old_print(*caps)


words = ('black', 'white', 'grey', 'black-1', 'white-1', 'python')
print(*words, sep=' to ', end=' LOVE')
