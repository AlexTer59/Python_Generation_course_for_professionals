import calendar
year, month = input().split()
year = int(year)
month = list(calendar.month_name).index(month)
print(calendar.monthrange(year, month)[1])