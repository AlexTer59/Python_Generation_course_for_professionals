from datetime import date
def is_correct(day, month, year):
    try:
        my_date = date(year, month, day)
    except ValueError:
        return False
    return True




print(is_correct(31, 12, 2021))