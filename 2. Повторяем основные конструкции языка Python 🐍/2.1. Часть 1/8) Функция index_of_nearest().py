def index_of_nearest(numbers, number):
    if len(numbers) == 0:
        return -1
    else:
        numbers = list(map(lambda x: abs(x - number), numbers))
        return numbers.index(min(numbers))

print(index_of_nearest([9, 5, 3, 2, 11], 4))