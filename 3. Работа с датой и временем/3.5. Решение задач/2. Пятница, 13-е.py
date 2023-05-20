from datetime import datetime
res = {'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0,'Saturday': 0, 'Sunday': 0}
start_date = datetime.strptime('01.01.0001', '%d.%m.%Y')
end_date = datetime.strptime('31.12.9999', '%d.%m.%Y')
