def choose_plural(amount, declensions):
    if amount % 10 in (0,5,6,7,8,9) or amount % 100 in (10,11,12,13,14,15,16,17,18,19,20):
        return str(amount) + ' ' + declensions[2]
    elif amount % 10 in (2,3,4):
        return str(amount) + ' ' + declensions[1]
    else:
        return str(amount) + ' ' + declensions[0]



assert (choose_plural(21, ('пример', 'примера', 'примеров'))) == '21 пример'
assert choose_plural(92, ('гвоздь', 'гвоздя', 'гвоздей')) == '92 гвоздя'
assert (choose_plural(8, ('яблоко', 'яблока', 'яблок'))) == '8 яблок'
assert (choose_plural(111223, ('копейка', 'копейки', 'копеек'))) == '111223 копейки'
assert (choose_plural(763434, ('рубль', 'рубля', 'рублей'))) == '763434 рубля'
assert (choose_plural(512312, ('цент', 'цента', 'центов'))) == '512312 центов'
assert (choose_plural(59, ('помидор', 'помидора', 'помидоров'))) == '59 помидоров'
assert (choose_plural(23424157, ('огурец', 'огурца', 'огурцов'))) == '23424157 огурцов'
assert (choose_plural(240, ('курица', 'курицы', 'куриц'))) == '240 куриц'
assert (choose_plural(49324, ('плюмбус', 'плюмбуса', 'плюмбусов'))) == '49324 плюмбуса'
assert (choose_plural(505, ('утка', 'утки', 'уток'))) == '505 уток'
assert (choose_plural(666, ('шкаф', 'шкафа', 'шкафов'))) == '666 шкафов'
assert (choose_plural(11, ('стул', 'стула', 'стульев'))) == '11 стульев'
assert (choose_plural(3458438435812, ('доллар', 'доллара', 'долларов'))) == '3458438435812 долларов'
assert (choose_plural(2, ('пример', 'примера', 'примеров'))) == '2 примера'
assert (choose_plural(111, ('пример', 'примера', 'примеров'))) == '111 примеров'
assert (choose_plural(1223123111, ('пример', 'примера', 'примеров'))) == '1223123111 примеров'