from datetime import date
dates = [date.fromisoformat(input()) for _ in range(int(input()))]
for i in sorted(dates):
    print(i.strftime('%d/%m/%Y'))