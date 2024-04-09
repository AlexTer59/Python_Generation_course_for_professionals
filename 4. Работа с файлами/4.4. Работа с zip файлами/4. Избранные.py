'''
Вам доступен архив workbook.zip, содержащий различные папки и файлы. Напишите программу, которая выводит названия
файлов из этого архива, которые были созданы или изменены позднее 2021-11-30 14:22:00. Названия файлов должны быть
расположены в лексикографическом порядке, каждое на отдельной строке.

Примечание 1. Если файл находится в папке, вывести следует только название без пути.

Примечание 2. Начальная часть ответа выглядит так:

countries.json
data_sample.csv
...
'''

from zipfile import ZipFile
from datetime import datetime

DATE = datetime(year=2021, month=11, day=30, hour=14, minute=22, second=0)
with ZipFile('4. workbook.zip') as zip_file:
    print(*sorted([i.filename.rsplit('/', maxsplit=1)[-1] for i in zip_file.infolist() if
                   datetime(*i.date_time) > DATE and not i.is_dir()]), sep='\n')
