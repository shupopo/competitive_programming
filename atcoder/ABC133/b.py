import math
N, D = map(int, input().split())
coordinates = []
count = 0
for i in range(N):
    coordinate = [int(i) for i in input().split()]
    coordinates.append(coordinate)

for i in range(N):
    for j in range(i + 1, N):
        distance = 0
        for k in range(D):
            distance += abs(coordinates[i][k] - coordinates[j][k]) ** 2
        distance = math.sqrt(distance)
        if distance.is_integer():
            count += 1
print(count)
