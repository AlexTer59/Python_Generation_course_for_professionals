'''
Для дополнительного заработка Тимур решил заняться продажей овощей. У него имеются данные о продажах за год,
разделенные на четыре файла по кварталам: quarter1.csv, quarter2.csv, quarter3.csv и quarter4.csv. В каждом файле
в первом столбце указывается название продукта, а в последующих — количество проданного продукта в килограммах за
определенный месяц:

продукт,январь,февраль,март
Картофель,39,61,3
Дайкон,51,96,83
...
Также присутствует файл prices.json, содержащий словарь, в котором ключом является название продукта, а
значением — цена за килограмм в рублях:

{
   "Картофель": 53,
   "Дайкон": 55,
...
}
Напишите программу, которая выводит единственное число — сумму, заработанную Тимуром за год на продаже овощей.
'''

from collections import Counter
import csv
import json


total_earned = Counter()
with open('10. prices.json', encoding='UTF-8') as prices:
    price = json.load(prices)
for i in range(1, 5):
    with open(f'10. quarter{str(i)}.csv', 'r', encoding='UTF-8') as quarter:
        _, *data = csv.reader(quarter)
    data = {k: sum(map(int, v)) * price[k] for k, *v in data}
    total_earned += data
print(sum(total_earned.values()))
