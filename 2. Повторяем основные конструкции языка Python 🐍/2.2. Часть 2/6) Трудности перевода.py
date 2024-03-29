list_sets = [set(i for i in input().split(', ')) for _ in range(int(input()))]
res_set = list_sets[0]
for i in range(1, len(list_sets)):
    res_set &= list_sets[i]
if res_set:
    print(*sorted(res_set), sep=', ')
else:
    print('Сериал снять не удастся')
