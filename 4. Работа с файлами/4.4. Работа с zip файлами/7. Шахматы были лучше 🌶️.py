'''
Вам доступен архив data.zip, содержащий различные папки и файлы. Среди них есть несколько JSON файлов, каждый из
которых содержит информацию о каком-либо футболисте:

{
   "first_name": "Gary",
   "last_name": "Cahill",
   "team": "Chelsea",
   "position": "Defender"
}
У футболиста имеются следующие атрибуты:

first_name — имя
last_name — фамилия
team — название футбольного клуба
position — игровая позиция
Напишите программу, которая обрабатывает только данные JSON файлы и выводит имена и фамилии футболистов, выступающих за
футбольный клуб Arsenal. Футболисты должны быть расположены в лексикографическом порядке имен, а при совпадении — в
лексикографическом порядке фамилий, каждый на отдельной строке.

Примечание 1. Обратите внимание, что наличие у файла расширения .json не гарантирует, что он является корректным
текстовым файлом в формате JSON. Для того чтобы определить, является ли файл корректным текстовым файлом в формате
JSON, воспользуйтесь конструкцией try-except и функцией is_correct_json() из предыдущего урока.

Примечание 2. Начальная часть ответа выглядит так:

Alex Iwobi
Alexis Sanchez
...
'''

from zipfile import ZipFile
import json


def is_correct_json(string):
    try:
        json.loads(string)
    except json.decoder.JSONDecodeError:
        return False
    return True


player_list = []
with ZipFile('7. data.zip') as zip_file:
    for item in zip_file.infolist():
        if not item.is_dir() and item.filename.rsplit('.', maxsplit=1)[-1] == 'json':
            with zip_file.open(item.filename) as file:
                try:
                    reader = file.read().decode('UTF-8')
                    if is_correct_json(reader):
                        player_list.append(json.loads(reader))
                except:
                    continue

player_list = sorted(filter(lambda x: x['team'] == 'Arsenal', player_list),
                     key=lambda x: (x['first_name'], x['last_name']))
[print(f'{i["first_name"]} {i["last_name"]}') for i in player_list]