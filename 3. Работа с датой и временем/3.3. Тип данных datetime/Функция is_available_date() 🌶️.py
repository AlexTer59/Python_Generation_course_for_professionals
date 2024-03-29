from datetime import datetime


def date_to_arr(date):
    return set(i for i in range(datetime.strptime(date.split('-')[0], '%d.%m.%Y').toordinal(), datetime.strptime(
        date.split('-')[-1], '%d.%m.%Y').toordinal() + 1))


def is_available_date(booked_dates, date_for_booking):
    booked = set()
    for i in booked_dates:
        booked.update(date_to_arr(i))
    date_for_booking = date_to_arr(date_for_booking)
    if date_for_booking & booked:
        return False
    return True


dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021-04.11.2021'
print(is_available_date(dates, some_date))