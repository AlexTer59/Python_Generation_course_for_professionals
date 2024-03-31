'''
Дана последовательность целых чисел. Напишите программу, которая определяет, является ли данная последовательность
прогрессией, и если да, то определяет её вид.

Формат входных данных
На вход программе подается произвольное количество строк (не менее трёх), в каждой строке записано натуральное число
— очередной член последовательности.

Формат выходных данных
Программа должна вывести текст:

Арифметическая прогрессия, если введенная последовательность чисел является арифметической прогрессией
Геометрическая прогрессия, если введенная последовательность чисел является геометрической прогрессией
Не прогрессия, если введенная последовательность чисел не является прогрессией
'''

import sys


def is_arithmetic_progression(nums):
    diff = []
    for i in range(len(nums) - 1):
        diff.append(nums[i + 1] - nums[i])
    if len(set(diff)) == 1:
        return True
    return False


def is_geometric_progression(nums):
    diff = []
    for i in range(len(nums) - 1):
        diff.append(nums[i + 1] / nums[i])
    if len(set(diff)) == 1:
        return True
    return False


numbers = [int(line.strip()) for line in sys.stdin]
if is_arithmetic_progression(numbers):
    print('Арифметическая прогрессия')
elif is_geometric_progression(numbers):
    print('Геометрическая прогрессия')
else:
    print('Не прогрессия')
