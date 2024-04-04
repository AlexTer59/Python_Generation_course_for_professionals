'''
Вам доступен файл data.json, содержащий список различных объектов:

[
   "nwkWXma",
   null,
   {
      "ISgHT": "dIUbf"
   },
   "Pzt",
   "BXcbGVTE",
   ...
]
Напишите программу, которая создает список, элементами которого являются объекты из списка, содержащегося в файле
data.json, измененные по следующим правилам:

если объект является строкой, в его конец добавляется восклицательный знак
если объект является числом, он увеличивается на единицу
если объект является логическим значением, он инвертируется
если объект является списком, он удваивается
если объект является JSON-объектом (словарем), в него добавляется новая пара "newkey": null
если объект является пустым значением (null), он не добавляется
Полученный список программа должна записать в файл updated_data.json.
'''

import json


with open('3. data.json', encoding='UTF-8') as file:
    py_list = json.loads(file.read())
res_list = []
for i in py_list:
    match i:
        case str(): i += '!'
        case bool(): i = not i
        case int(): i += 1
        case list(): i *= 2
        case dict(): i['newkey'] = None
        case None: continue
    res_list.append(i)

with open('3. updated_data.json', 'w', encoding='UTF-8') as file:
    json.dump(res_list, file)
