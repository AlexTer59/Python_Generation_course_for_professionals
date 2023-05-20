import calendar
year, month = input().split()
month = list(calendar.month_abbr).index(month)
print(calendar.month(int(year), month))