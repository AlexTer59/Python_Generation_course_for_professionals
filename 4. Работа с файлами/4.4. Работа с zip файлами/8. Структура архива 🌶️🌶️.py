'''
Вам доступен архив desktop.zip, содержащий различные папки и файлы. Напишите программу, которая выводит его файловую
структуру и объем каждого файла.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести файловую структуру архива desktop.zip и объем каждого файла в несжатом виде. Так как архив
имеет собственную иерархию папок, каждый уровень вложенности должен быть выделен двумя пробелами.

Примечание 1. Вывод на примере архива test.zip из конспекта:

test
  Картинки
    1.jpg 88 KB
    avatar.png 19 KB
    certificate.png 43 KB
    py.png 33 KB
    World_Time_Zones_Map.png 2 MB
    Снимок экрана.png 11 KB
  Неравенства.djvu 5 MB
  Программы
    image_util.py 5 KB
    sort.py 61 B
  Разные файлы
    astros.json 505 B
Примечание 2. Объем файла записывается в самых крупных единицах измерения с округлением до целых.

Примечание 3. Значения единиц измерения такие же, какие приняты в информатике:

1 KB = 1024 B
1 MB = 1024 KB
1 GB = 1024 MB
'''
from zipfile import ZipFile


def to_true_size_type(size):
    size = int(size)
    types = ['B', 'KB', 'MB', 'GB']
    counter = 0
    while size // 1024 > 0:
        if counter == 3:
            return f'{round(size)} GB'
        else:
            size /= 1024
            counter += 1
    return f'{round(size)} {types[counter]}'


space = '  '
with ZipFile('8. desktop.zip') as zip_file:
    for item in zip_file.infolist():
        if not item.is_dir():
            print(space * (len(item.filename.split('/')) - 1) + item.filename.split('/')[-1],
                  to_true_size_type(item.file_size))
        else:
            print(space * (len(item.filename.split('/')) - 2) + item.filename.split('/')[-2])
