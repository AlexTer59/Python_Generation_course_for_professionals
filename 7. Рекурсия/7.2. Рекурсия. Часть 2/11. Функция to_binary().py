'''
Реализуйте функцию to_binary() с использованием рекурсии, которая принимает один аргумент:

number — неотрицательное целое число
Функция должна возвращать строковое представление числа number в двоичной системе счисления.
'''

def to_binary(number):
    if number < 2:
        return str(number % 2)
    return to_binary(number // 2) + str(number % 2)

print(to_binary(16))