L, R = map(int, input().split())
ans = 0

if L // 2019 < R // 2019:
    print(ans)
    exit()

ans = 2018
for i in range(L, R + 1):
    for j in range(i + 1, R + 1):
        tmp = (i * j) % 2019
        if tmp < ans:
            ans = tmp
print(ans)
