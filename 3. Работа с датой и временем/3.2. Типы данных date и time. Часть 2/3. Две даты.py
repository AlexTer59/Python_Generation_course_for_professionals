from datetime import date
date1, date2 = date.fromisoformat(input()), date.fromisoformat(input())
print(min([date1, date2]).strftime('%d-%m (%Y)'))
