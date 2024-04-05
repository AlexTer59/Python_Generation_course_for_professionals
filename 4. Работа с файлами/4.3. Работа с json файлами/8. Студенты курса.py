'''
Вам доступен файл students.json, содержащий список JSON-объектов, которые представляют данные о студентах некоторого курса:

[
   {
      "name": "Holly-Anne",
      "city": "Abilene",
      "age": 29,
      "progress": 85,
      "phone": "(802) 983-9126"
   },
   ...
]
Под «студентом» мы будем подразумевать один JSON-объект из этого списка. У студента имеются следующие атрибуты:

name — имя
city — город проживания
age — возраст
progress — прогресс по курсу в процентах
phone— контактный номер
Напишите программу, которая определяет студентов, удовлетворяющих следующим условиям:

возраст 18 лет или более
прогресс по курсу 75% или более
Программа должна создать файл data.csv с двумя столбцами — name (имя) и phone (номер), и записать в него данные
выбранных студентов, расположив их в лексикографическом порядке имён. В качестве разделителя в файле data.csv должна
быть использована запятая.

Примечание 1. Гарантируется, что все студенты имеют различные имена.

Примечание 2. Начальная часть файла data.csv выглядит так:

name,phone
Cary,(580) 476-8517
Catarina,(237) 608-2757
Catherin,(876) 215-3666
...
'''

import csv
import json

with open('8. students.json', encoding='UTF-8') as file:
    py_students = json.load(file)
data = []
for item in py_students:
    if item['age'] >= 18 and item['progress'] >= 75:
        data.append([item['name'], item['phone']])
with open('8. data.csv', 'w', encoding='UTF-8') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'phone'])
    writer.writerows(sorted(data, key=lambda x: x[0]))

