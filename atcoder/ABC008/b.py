N = int(input())
candidates = {}
for i in range(N):
    S = input()
    if S in candidates.keys():
        candidates[S] += 1
    else:
        candidates[S] = 1
print(max(candidates, key=candidates.get))
