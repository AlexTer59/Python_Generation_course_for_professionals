'''
Вам доступен файл data.csv, который содержит неповторяющиеся данные о пользователях некоторого ресурса.
В первом столбце записано имя пользователя, во втором — фамилия, в третьем — адрес электронной почты:

first_name,surname,email
John,Wilson,johnwilson@outlook.com
Mary,Wilson,marywilson@list.ru
...
Напишите программу, которая создает файл domain_usage.csv, имеющий следующее содержание:

domain,count
rambler.ru,24
iCloud.com,29
...
где в первом столбце записано название почтового домена, а во втором — количество пользователей, использующих данный
домен. Домены в файле должны быть расположены в порядке возрастания количества их использований, при совпадении
количества использований — в лексикографическом порядке.

Примечание 1. Разделителем в файле data.csv является запятая, при этом кавычки не используются.
'''

with open('5. data.csv', 'r', encoding='UTF-8') as f:
    dct = {}
    for line in f.readlines()[1:]:
        domain = line[line.index('@') + 1:].strip()
        dct[domain] = dct.get(domain, 0) + 1
sort_domain = sorted(dct, key=lambda x: (int(dct[x]), x))

with open('5. domain_usage.csv', 'w', encoding='UTF-8') as f:
    print('domain,count', file=f)
    for i in sort_domain:
        print(i, dct[i], sep=',', file=f)

