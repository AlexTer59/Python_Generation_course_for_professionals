'''
Вам доступны два файла data1.json и data2.json, каждый из которых содержит по единственному JSON-объекту:

{
   "Holly-Anne": [
      33,
      "failed"
   ],
   "Caty": [
      36,
      "failed"
   ],
   ...
}
Напишите программу, которая объединяет два данных JSON-объекта в один JSON-объект, причем если пары из первого и
второго объектов имеют совпадающие ключи, то значение следует взять из второго объекта. Полученный JSON-объект
программа должна записать в файл data_merge.json.

Примечание 1. Например, если бы файлы data1.json и data2.json имели вид:

{
   "Timur": 99,
   "Anri": 97
}
{
   "Dima": 99,
   "Anri": 100
}
то программа должна была бы создать файл data_merge.json со следующим содержанием:

{
   "Anri": 100,
   "Dima": 99,
   "Timur": 99
}
Примечание 2. Элементы в результирующем JSON-объекте могут располагаться в произвольном порядке.
'''


import json

with open('data1.json', encoding='UTF-8') as file1, open('data2.json', encoding='UTF-8') as file2:
    new_data = {**json.loads(file1.read()), **json.loads(file2.read())}
with open('data_merge', 'w', encoding='UTF-8') as file:
    json.dump(new_data, file)