'''
Число 13 считалось дьявольским издавна. Это имеет свое объяснение, и не одно: тут есть трактовки, связанные с Тайной вечерей — где были Христос и
12 апостолов, один из которых стал предателем. Есть поверье, что для шабаша нужны
12 ведьм и сатана. В истории число 13 в связке с пятницей стало «несчастливым» в
1307 году, когда король Франции Филипп Красивый отдал приказ схватить всех тамплиеров — членов рыцарского
ордена крестоносцев. Все они были сожжены на кострах инквизиции, и произошло это в пятницу, 13 апреля.

Докажите, что 13-е число месяца чаще всего приходится на пятницу. Напишите программу, которая вычисляет,
сколько тринадцатых чисел приходится на каждый день недели в период с 01.01.0001 по 31.12.9999.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна вывести 7 чисел — количество тринадцатых чисел, которые приходятся на понедельник,
вторник, среду, четверг, пятницу, субботу и воскресенье в период с 01.01.0001 по 31.12.9999.
Числа должны быть расположены каждое на отдельной строке.
'''

from datetime import datetime

days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
res = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}
for year in range(1, 9999 + 1):
    for month in range(1, 12 + 1):
        res[datetime(day=13, month=month, year=year).isoweekday()] += 1
print(*res.values(), sep='\n')
