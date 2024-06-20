'''
Вам доступен список data, содержащий произвольные объекты. Дополните приведенный ниже код, чтобы он вывел все числа
(тип int и float), находящиеся в данном списке, отбрасывая дробную часть у вещественных чисел. Числа должны быть
расположены в своем исходном порядке, каждое на отдельной строке.

Примечание 1. Начальная часть ответа выглядит так:

-16
-202
883
...
Примечание 2. В задаче удобно воспользоваться функциями map() и filter().

data = ['Timur', -16.648911695768902, 'six', -202, 883.0093275936454, -765, (3, 4), -105.10718000213546, 976,
-308.96857946288094, 458, ['one', 'two'], 479.92207220345927, -87, -71, 'twelve', 112, -621, -715.0179551194733,
'seven', 229, 729, -358, [1, 2, 3], -974, 882, -894.4709033242768, '', 323.7720806756133, 'beegeek', -224, 431,
170.6353248658936, -343.0016746052049, 'number', 104.17133679352878, [], -353.5964777099863, 'zero', -113, 288,
None, -708.3036176571618]
'''

data = ['Timur', -16.648911695768902, 'six', -202, 883.0093275936454, -765, (3, 4), -105.10718000213546, 976,
-308.96857946288094, 458, ['one', 'two'], 479.92207220345927, -87, -71, 'twelve', 112, -621, -715.0179551194733,
'seven', 229, 729, -358, [1, 2, 3], -974, 882, -894.4709033242768, '', 323.7720806756133, 'beegeek', -224, 431,
170.6353248658936, -343.0016746052049, 'number', 104.17133679352878, [], -353.5964777099863, 'zero', -113, 288,
None, -708.3036176571618]

print(*map(int, filter(lambda x: type(x) is int or type(x) is float, data)), sep='\n')
