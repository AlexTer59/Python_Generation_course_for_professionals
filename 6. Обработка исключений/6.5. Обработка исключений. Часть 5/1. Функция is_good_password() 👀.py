'''
Назовем пароль хорошим, если

его длина равна 9 или более символам
в нем присутствуют большие и маленькие буквы любого алфавита
в нем имеется хотя бы одна цифра
Реализуйте функцию is_good_password() в стиле LBYL, которая принимает один аргумент:

string — произвольная строка
Функция должна возвращать True, если строка string представляет собой хороший пароль, или False в противном случае.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_good_password(), но не
код, вызывающий ее.
'''


def is_good_password(string):
    return len(string) >= 9 and \
           any([True for i in string if i.islower()]) and \
           any([True for i in string if i.isupper()]) and \
           any([True for i in string if i.isdigit()])
