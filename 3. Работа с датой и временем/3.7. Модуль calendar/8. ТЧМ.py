import calendar
from datetime import date
def get_all_mondays(year):
    thursdays = []
    for month in range(1, 13):
        counter = 0
        for week in calendar.monthcalendar(year, month):
            thursday = week[3]
            if thursday:
                counter += 1
                if counter == 3:
                    #thursdays.append(date.strftime(year, month, thursday))
                    thursdays.append(date(year, month, thursday).strftime('%d.%m.%Y'))
    return thursdays




print(*get_all_mondays(int(input())), sep='\n')