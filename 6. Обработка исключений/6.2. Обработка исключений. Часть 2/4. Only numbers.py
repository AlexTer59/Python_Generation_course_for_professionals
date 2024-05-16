'''
На вход программе подается неопределенное количество строк, каждая из которых содержит произвольное значение.
Напишите программу с использованием конструкции try-except, которая выводит сумму всех введенных чисел,
а затем — количество введенных нечисловых значений.

Формат входных данных
На вход программе подается неопределенное количество строк (хотя бы одна), каждая из которых содержит произвольное
значение.

Формат выходных данных
Программа должна вывести сумму всех введенных чисел (тип int и float), а затем на следующей строке — количество
введенных нечисловых значений.

Примечание 1. Если ни одно число введено не было, то сумма равна 0.

Примечание 2. Рассмотрим первый тест. Имеем три введенных числа, сумма которых равна: 100+10+1.1=111.1
Также три нечисловых значения, а именно: i'm number!, [1, 99], {'math', 'physics'}.
'''

import sys

not_numbers = nums_sum = 0

for i in sys.stdin:
    try:
        nums_sum += float(i)
    except ValueError:
        not_numbers += 1

print(int(nums_sum) if nums_sum == int(nums_sum) else nums_sum)
print(not_numbers)

