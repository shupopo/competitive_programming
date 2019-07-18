N, L = map(int, input().split())

apples = []
apples_abs = []

for i in range(1, N+1):
    apple = L+i - 1
    apples.append(apple)
    apples_abs.append(abs(apple))

min_apple_idx = apples_abs.index(min(apples_abs))
apples.pop(min_apple_idx)
print(sum(apples))
