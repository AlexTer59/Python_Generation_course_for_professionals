import calendar
year, month = input().split()
print((calendar.monthrange(int(year), int(month)))[1])