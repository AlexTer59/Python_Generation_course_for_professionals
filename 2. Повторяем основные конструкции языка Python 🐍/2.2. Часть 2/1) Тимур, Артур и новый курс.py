def minimal_distance(distance):
    if max(distance) > sum(distance) - max(distance):
        return (sum(distance) - max(distance)) * 2
    else:
        return sum(distance)


d1, d2, d3 = int(input()), int(input()), int(input())
print(minimal_distance([d1, d2, d3]))