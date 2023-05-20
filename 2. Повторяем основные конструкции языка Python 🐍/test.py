from functools import reduce
print(reduce(lambda acc, x: acc + x if x >= 0 else acc, [int(input()) for i in range(3)]), 0)

#print(list[10])
#str = 'Hello'
#print(str[0])
#[1,-2,3]
#[1,3]
#[6]
#list = [2,3,5,-220]
#sum = 0
#for i in list:
    #sum = sum + i
    #1) 0 = 0 + 2 sum = 2
    #2) 2 = 2 + 3 s