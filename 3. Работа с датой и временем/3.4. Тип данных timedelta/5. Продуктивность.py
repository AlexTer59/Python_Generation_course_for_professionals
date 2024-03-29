from datetime import datetime, timedelta
pattern = '%d.%m.%Y'
start_date = datetime.strptime(input(), pattern)
for i in range(2, 12):
    print(start_date.strftime(pattern))
    start_date = start_date + timedelta(days=i)
    #print((start_date + timedelta(days=i)).strftime(pattern))