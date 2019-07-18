txa, tya, txb, tyb, T, V = map(int, input().split())
n = int(input())
max_distance = T*V
for _ in range(n):
    x, y = map(int, input().split())
    distance1 = sqrt((x - txa) ** 2 + (y - tya) ** 2)
    distance2 = sqrt((txb-x) ** 2 + (tyb-y) ** 2)
    if distance1 + distance2 <= max_distance:
        print("YES")
        exit()
    else:
        continue
print("NO")
