employers = [input() for i in range(int(input()))]
new_employers = [input() for i in range(int(input()))]
for i in range(len(new_employers)):
    counter = 0
    tmp = new_employers[i]
    while any(map(lambda x: (tmp + '@beegeek.bzz') in x, employers)):
        tmp = new_employers[i]
        counter += 1
        tmp += str(counter)
    new_employers[i] = tmp + '@beegeek.bzz'
    employers.append(new_employers[i])
print(*new_employers, sep='\n')
