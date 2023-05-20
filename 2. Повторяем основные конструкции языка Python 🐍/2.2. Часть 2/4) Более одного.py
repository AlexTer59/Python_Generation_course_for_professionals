nums = input().split()
my_dict = {i: 0 for i in nums}
more_one = []
for i in nums:
    my_dict[i] += 1
for key, value in my_dict.items():
    if value > 1:
        more_one.append(int(key))
print(*sorted(more_one))
