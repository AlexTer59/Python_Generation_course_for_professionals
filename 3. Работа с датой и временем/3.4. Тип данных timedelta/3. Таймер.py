from datetime import timedelta, datetime
pattern = '%H:%M:%S'
time = datetime.strptime(input(), pattern)
print((time + timedelta(seconds=int(input()))).strftime(pattern))