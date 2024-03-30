'''
Команда BEEGEEK планирует выпустить свой новый курс 08.11.2022 ровно в 12:00. Напишите программу,
которая принимает на вход текущие дату и время и определяет, сколько времени осталось до выхода курса.

Формат входных данных
На вход программе подаются текущие дата и время в формате DD.MM.YYYY HH:MM.

Формат выходных данных
Программа должна вывести текст с указанием количества дней и часов, оставшихся до выхода курса, в следующем формате:

До выхода курса осталось: <кол-во дней> дней и <кол-во часов> часов
Если в данном случае количество часов равно нулю, то вывести нужно только дни.

Если количество дней равно нулю, то вывести нужно только часы и минуты в следующем формате:

До выхода курса осталось: <кол-во часов> часов и <кол-во минут> минут
Если в данном случае количество минут равно нулю, то вывести нужно только часы. Аналогично, если количество
часов равно нулю, то вывести нужно только минуты.

Если введенные дата и время больше либо равны 08.11.2022 12:00, программа должна вывести текст:

Курс уже вышел!
'''
from datetime import datetime


def choose_plural(amount, declensions):
    if amount % 10 in (0, 5, 6, 7, 8, 9) or amount % 100 in (10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20):
        return str(amount) + ' ' + declensions[2]
    elif amount % 10 in (2, 3, 4):
        return str(amount) + ' ' + declensions[1]
    else:
        return str(amount) + ' ' + declensions[0]


REALISE_DATE = datetime(day=8, month=11, year=2022, hour=12)
DAYS = ("день", "дня", "дней")
HOURS = ("час", "часа", "часов")
MINUTES = ("минута", "минуты", "минут")

current_date = datetime.strptime(input(), '%d.%m.%Y %H:%M')
if current_date >= REALISE_DATE:
    print('Курс уже вышел!')
else:
    difference = REALISE_DATE - current_date
    true_days = choose_plural(difference.days, DAYS)
    true_hours = choose_plural((difference.seconds // 3600), HOURS)
    true_minutes = choose_plural(int((difference.seconds / 60) % 60), MINUTES)
    if difference.days == 0:
        print(f'До выхода курса осталось:'
              f' {" и ".join([i for i in [true_hours, true_minutes] if not i.startswith("0")])}')
    else:
        print(f'До выхода курса осталось:'
              f' {" и ".join([i for i in [true_days, true_hours] if not i.startswith("0")])}')
