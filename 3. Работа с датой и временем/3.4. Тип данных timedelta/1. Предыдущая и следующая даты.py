from datetime import datetime, timedelta, date
date = datetime.strptime(input(), '%d.%m.%Y')
print(((date - timedelta(days=1)).strftime('%d.%m.%Y')))
print(((date + timedelta(days=1)).strftime('%d.%m.%Y')))
