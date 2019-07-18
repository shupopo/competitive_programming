N = int(input())

shortage = 2025-N
candidates = []
for i in range(1, 10):
    for j in range(1, 10):
        if i * j == shortage:
            candidates.append(str(i) + " x " + str(j))
for candidate in candidates:
    print(candidate)
