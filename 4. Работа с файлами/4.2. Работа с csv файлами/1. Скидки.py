import csv

with open("sales.csv", 'r', encoding='UTF-8') as file:
    data = csv.DictReader(file, delimiter=';')
    print(*[row['name'] for row in data if int(row['old_price']) > int(row['new_price'])], sep='\n')
