'''
Вам доступен текстовый файл pythonzen.txt, содержащий текст на английском языке:

The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
...
Напишите программу, которая определяет, сколько раз встречается каждая буква в этом тексте. Буквы и их количество
должны выводиться в лексикографическом порядке, каждая на отдельной строке, в следующем формате:

<буква>: <количество>
Примечание 1. Начальная часть ответа выглядит так:

a: 53
b: 21
...
Примечание 2. Программа не должна учитывать регистр, то есть, например, буквы a и A считаются одинаковыми.

Примечание 3. Программа должна игнорировать все небуквенные символы.
'''

from collections import Counter

with open('5. pythonzen.txt', 'r', encoding='UTF-8') as file:
    letters = [letter.lower() for letter in file.read() if letter.isalpha()]
for k, v in sorted(Counter(letters).items()):
    print(f'{k}: {v}')
