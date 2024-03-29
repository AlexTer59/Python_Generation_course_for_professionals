from datetime import date
def is_correct(day, month, year):
    try:
        my_date = date(int(year), int(month), int(day))
    except ValueError:
        return False
    return True

counter = 0
str = input()
while str != 'end':
    day, month, year = str.split('.')
    if is_correct(day, month, year):
        print('Корректная')
        counter += 1
    else:
        print('Некорректная')
    str = input()
print(counter)