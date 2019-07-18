n = int(input())
petals = [int(i) for i in input().split()]
count = 0

for petal in petals:
    if petal % 2 == 0:
        if petal - 1 % 5 == 0:
            count += 2
        else:
            count += 1
    else:
        if petal % 5 == 0:
            count += 2
        else:
            continue

print(count)
