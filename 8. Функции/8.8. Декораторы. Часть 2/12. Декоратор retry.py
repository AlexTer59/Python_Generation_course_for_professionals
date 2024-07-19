'''
Реализуйте декоратор retry, который принимает один аргумент:

times — натуральное число
Декоратор должен выполнять повторную попытку вызова декорируемой функции, если во время ее выполнения возникает ошибка.
Декоратор должен вызывать ее до тех пор, пока не исчерпает количество попыток times, после чего должен возбуждать
исключение MaxRetriesException.

Также декоратор должен сохранять имя и строку документации декорируемой функции.

Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а
также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор retry, но не код,
вызывающий его.
'''
import functools


class MaxRetriesException(Exception):
    pass


def retry(times):
    def decorator(func):
        func.__dict__['times'] = 0

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception:
                func.__dict__['times'] += 1
                while func.__dict__['times'] < times:
                    return wrapper(*args, **kwargs)
                raise MaxRetriesException
        return wrapper
    return decorator

