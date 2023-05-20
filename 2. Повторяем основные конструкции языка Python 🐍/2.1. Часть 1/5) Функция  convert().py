from string import *
def convert(string):
    lower = len(list(filter(lambda x: x in ascii_lowercase, string)))
    upper = len(list(filter(lambda x: x in ascii_uppercase, string)))
    return string.upper() if upper > lower else string.lower()


string = input()
print(convert(string))