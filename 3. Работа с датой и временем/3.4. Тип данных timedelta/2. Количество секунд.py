from datetime import datetime, timedelta
pattern = '%H:%M:%S'
time = datetime.strptime(input(), pattern)
print(int(timedelta(hours=time.hour, minutes=time.minute, seconds=time.second).total_seconds()))