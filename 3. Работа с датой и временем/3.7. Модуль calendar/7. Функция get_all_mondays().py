import calendar
from datetime import date, timedelta
def get_all_mondays(year):
    days = []
    if calendar.monthrange(year, 1)[0] == 0:
        this_date = date(year, 1, 1 + (calendar.monthrange(year, 1)[0]))
    else:
        this_date = date(year, 1, 1 + (abs(calendar.monthrange(year, 1)[0] - 7)))
    while this_date.year != year + 1:
        days.append(this_date)
        this_date += timedelta(days=7)
    return days


print(get_all_mondays(111))