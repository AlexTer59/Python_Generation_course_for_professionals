from datetime import date, timedelta


def num_of_sundays(year):
    counter, td = 0, timedelta(days=7)
    d = date(year=year, month=1, day=1)
    d += timedelta(days=6 - d.weekday())
    while year == d.year:
        d += td
        counter += 1
    return counter


print(num_of_sundays(2023))
