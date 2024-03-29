from datetime import date
def saturdays_between_two_dates(date1, date2):
    counter = 0
    if date1 < date2:
        for i in range(date1.toordinal(), date2.toordinal() + 1):
            if date.fromordinal(i).weekday() == 5:
                counter += 1
        return counter
    else:
        for i in range(date2.toordinal(), date1.toordinal() + 1):
            if date.fromordinal(i).weekday() == 5:
                counter += 1
        return counter




date1 = date(2020, 7, 26)
date2 = date(2020, 7, 2)

print(saturdays_between_two_dates(date1, date2))