'''
Требовалось реализовать функцию get_max_index(), которая принимает в качестве аргумента список различных целых чисел и
возвращает индекс наибольшего числа из этого списка (начиная с 0). Программист торопился и реализовал функцию
неправильно.

Найдите и исправьте все ошибки, допущенные в реализации этой функции (их ровно 4).

Примечание. Известно, что каждая ошибка затрагивает только одну строку и может быть исправлена без изменения других
строк

def get_max_index(numbers):
    max_index = 0
    max_value = numbers[-1]

    for index, value in enumerate(numbers, 1):
        if index > max_index:
            max_index = index
            max_value = value

    return max_value
'''

def get_max_index(numbers):
    max_index = 0
    max_value = numbers[0]

    for index, value in enumerate(numbers):
        if value > max_value:
            max_index = index
            max_value = value

    return max_index
