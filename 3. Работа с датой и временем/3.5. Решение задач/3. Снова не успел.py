'''
Дан режим работы магазина:

Понедельник	9:00 - 21:00
Вторник	9:00 - 21:00
Среда	9:00 - 21:00
Четверг	9:00 - 21:00
Пятница	9:00 - 21:00
Суббота	10:00 - 18:00
Воскресенье	10:00 - 18:00
Напишите программу, которая принимает на вход текущие дату и время и определяет количество минут, оставшееся до закрытия магазина.

Формат входных данных
На вход программе подаются текущие дата и время в формате DD.MM.YYYY HH:MM.

Формат выходных данных
Программа должна вывести количество минут, которое осталось до закрытия магазина, или текст Магазин не работает, если он закрыт.
'''

from datetime import datetime, timedelta

date_and_time = datetime.strptime(input(), '%d.%m.%Y %H:%M')
td = timedelta(hours=date_and_time.hour, minutes=date_and_time.minute)
if date_and_time.weekday() < 5 and timedelta(hours=9) <= td < timedelta(hours=21):
    print((timedelta(hours=21) - td).seconds // 60)
elif date_and_time.weekday() >= 5 and timedelta(hours=10) <= td < timedelta(hours=18):
    print((timedelta(hours=18) - td).seconds // 60)
else:
    print('Магазин не работает')
