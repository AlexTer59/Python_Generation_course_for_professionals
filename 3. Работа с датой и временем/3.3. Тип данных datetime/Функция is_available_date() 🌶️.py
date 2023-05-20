from datetime import datetime
def is_available_date():
    for i in dates:
        pass




dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021'
print(is_available_date(dates, some_date))



lst = [int(input()), int(input()), int(input())]
# lst = [1, 2, 3]
min_num = min(lst)
#min_num = 1
if min_num >= 0:
    print(sum(lst))
else:

from functools import reduce
    print(reduce(lambda x: if x > 0, lst))


