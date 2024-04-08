'''
Вам доступен файл food_services.json, содержащий список JSON-объектов, которые представляют данные о заведениях
общественного питания:

[
   {
      "Name": "СМЕТАНА",
      "IsNetObject": "нет",
      "OperatingCompany": "",
      "TypeObject": "кафе",
      "AdmArea": "Северо-Восточный административный округ",
      "District": "Ярославский район",
      "Address": "город Москва, улица Егора Абакумова, дом 9",
      "SeatsCount": 48
   },
   ...
]
Под «заведением» будем подразумевать один JSON-объект из этого списка. У заведения имеются следующие атрибуты:

Name — название
IsNetObject — да\нет в зависимости от того, является ли заведение сетевым
OperatingCompany — название сети
TypeObject — вид (кафе, столовая, ресторан и т.д.)
AdmArea — административная зона
District — район
Address — полный адрес
SeatsCount — количество мест
Напишите программу, которая:

определяет район Москвы, в котором находится больше всего заведений, и выводит название этого района и количество заведений в нем
определяет сеть с самым большим числом заведений и выводит название этой сети и количество заведений этой сети
Полученные значения программа должна вывести в следующем формате:

<район>: <количество заведений>
<название сети>: <количество заведений>
Примечание 1. Гарантируется, что искомая сеть единственная.

Примечание 2. Пример вывода:

район Метрогородок: 456
Французская пекарня SeDelice: 144
'''

import json

districts = {}
operating_companies = {}
with open('11. food_services.json', encoding='UTF-8') as file:
    reader = json.load(file)
    for item in reader:
        districts.setdefault(item['District'], 0)
        districts[item['District']] += 1
        if item['OperatingCompany'] != '':
            operating_companies.setdefault(item['OperatingCompany'], 0)
            operating_companies[item['OperatingCompany']] += 1
most_institution = max(districts, key=districts.get)
most_company = max(operating_companies, key=operating_companies.get)
print(f'{most_institution}: {districts.get(most_institution)}')
print(f'{most_company}: {operating_companies.get(most_company)}')
