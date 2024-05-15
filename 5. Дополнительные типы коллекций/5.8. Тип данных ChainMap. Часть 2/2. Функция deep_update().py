'''
Реализуйте функцию deep_update(), которая принимает три аргумента в следующем порядке:

chainmap — объект типа ChainMap, элементами которого являются словари
key — хешируемый объект
value — произвольный объект
Функция должна изменять все значения по ключу key во всех словарях в chainmap на value. Если ключ key отсутствует в
chainmap, функция должна добавить пару key: value в первый словарь.

Примечание 1. Функция должна изменять передаваемый объект типа ChainMap и возвращать значение None.

Примечание 2. Гарантируется, что передаваемый в функцию объект типа ChainMap содержит хотя бы один словарь.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию deep_update(), но не код,
вызывающий ее.
'''


from collections import ChainMap


def deep_update(chainmap, key, value):
    if key in chainmap:
        [dct.update({key: value}) for dct in chainmap.maps if key in dct]
    else:
        chainmap[key] = value



chainmap = ChainMap({'city': 'Moscow'}, {'name': 'Arthur'}, {'name': 'Timur'})
deep_update(chainmap, 'name', 'Dima')

print(chainmap)


