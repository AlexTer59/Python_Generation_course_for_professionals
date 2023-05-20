def likes (s):
    #print(names)
    if len(s) == 0:
        return 'Никто не оценил данную запись'
    elif len(s) == 1:
        return s[0] + ' оценил(а) данную запись'
    elif len(s) == 2 :
         return ' и '.join([i for i in s]) + ' оценили данную запись'
    elif len(s) == 3:
        return ', '.join([i for i in s[:2]]) + ' и ' + s[2] + ' оценили данную запись'
    elif len(s) >= 4:
       return ', '.join([i for i in s[:2]]) + ' и ' + str(len(s[2:])) + ' других оценили данную запись'



print(likes([]))
print(likes(['Тимур']))
print(likes(['Тимур', 'Артур']))
print(likes(['Тимур', 'Артур', 'Руслан']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'Дима', 'Рома', 'Гвидо', 'Марк']))