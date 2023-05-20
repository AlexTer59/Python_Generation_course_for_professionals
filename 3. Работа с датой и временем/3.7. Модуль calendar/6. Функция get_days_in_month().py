import calendar
from datetime import datetime, date
def get_days_in_month(year, month):
    month = list(calendar.month_name).index(month)
    dates = []
    for i in range(1, calendar.monthrange(year, month)[1] + 1):
        dates.append(datetime.strptime(str(year) + '.' + str(month) + '.' + str(i), '%Y.%m.%d').date())
    return dates



print(get_days_in_month(2021, 'December'))