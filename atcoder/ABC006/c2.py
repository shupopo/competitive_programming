N, M = map(int, input().split())

r = range(0, 10 ** 5)
x, z = 0, 0


# 老人0人と仮定した場合
for z in r:
    x = N - z
    if M - 2 * N == 2 * z and x >= 0:
        print(N - z, 0, z)
        exit()

# 老人1人と仮定した場合
for z in r:
    x = N - z - 1
    if M - 2 * N == 2 * z+1 and x >= 0:
        print(x, 1, z)
        exit()

print("-1 -1 -1")
