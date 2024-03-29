lst = [i for i in range(1, int(input()) + 1)]
dct = {}
#for i in lst:
    #dct.get(i, )

for i in range(1, len(lst)+1):
    lst[i - 1] = [int(i) for i in ' '.join(str(i)).split()]
for i in lst:
    dct[sum(i)] = dct.get(sum(i), 0) + 1
print(max(dct.values()))