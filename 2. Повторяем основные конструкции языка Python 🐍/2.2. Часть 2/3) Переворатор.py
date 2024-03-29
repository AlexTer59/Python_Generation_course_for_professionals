def rotator(n, X, Y, A, B):
    list = [i for i in range(1, n + 1)]
    list = list[:X - 1] + list[Y-(len(list))-1: X-(len(list))-2: -1] + list[Y:]
    list = list[:A - 1] + list[B-(len(list))-1: A-(len(list))-2: -1] + list[B:]
    return list


n, X, Y, A, B = [int(i) for i in input().split()]
print(*rotator(n, X, Y, A, B))