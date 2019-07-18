N, M = map(int, input().split())
r = range(0, 10**5)
for children in r:
    adults = -M + 3*N + children
    olds = M - 2 * N - 2 * children
    if adults >= 0 and olds >= 0:
        print(adults, olds, children)
        exit()
print("-1 -1 -1")
