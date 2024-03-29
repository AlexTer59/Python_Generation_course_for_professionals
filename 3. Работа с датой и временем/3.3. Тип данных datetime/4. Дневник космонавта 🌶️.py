from datetime import datetime
with open('diary.txt', 'r', encoding='utf-8') as file:
    dct = {}
    lst = (file.read().split('\n\n'))
    for i in lst:
        keys = i.split('\n', 1)[0]
        value = i.split('\n', 1)[1]
        keys = datetime.strptime(keys, '%d.%m.%Y; %H:%M')
        dct[keys] = value
    #print(dct)
    for key, value in sorted(dct.items()):
        print(datetime.strftime(key, '%d.%m.%Y; %H:%M'))
        print(value)
        print()

