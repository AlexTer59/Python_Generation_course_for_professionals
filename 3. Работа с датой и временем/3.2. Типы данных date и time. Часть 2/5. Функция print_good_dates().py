from datetime import date
def print_good_dates(dates):
    dates = list(sorted(filter(lambda x: x.year == 1992 and x.month + x.day == 29, dates)))
    for i in range(len(dates)):
        dates[i] = dates[i].strftime('%B %d, %Y')
    print(*dates, sep='\n')


dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
print_good_dates(dates)