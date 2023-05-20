def what_language(letters):
    num_let = [ord(i.upper()) for i in letters]
    print(num_let)
    if 1040 <= max(num_let) <= 1071 and 1040 <= min(num_let) <= 1071:
        return 'ru'
    elif 65 <= max(num_let) <= 90 and 65 <= min(num_let) <= 90:
        return 'en'
    else:
        return 'mix'

print(what_language([input(), input(), input()]))