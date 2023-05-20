def same_parity(numbers):
    if len(numbers) != 0:
        numbers = [int(i) for i in numbers]

        if numbers[0] % 2 == 0:
            numbers = list(filter(lambda x: x % 2 == 0, numbers))
        else:
            numbers = list(filter(lambda x: x % 2 != 0, numbers))

    return numbers

numbers = input().split(', ')
print(same_parity(numbers))