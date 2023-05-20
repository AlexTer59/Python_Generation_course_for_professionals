from string import *
def is_valid(string):
    if 4 <= len(string) <= 6:
        return all(False for i in string if i not in digits)
    else:
        return False






string = input()
print(is_valid(string))