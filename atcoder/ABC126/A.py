N, K = map(int, input().split())
S = list(input())

for i in range(len(S)):
    if i == K-1:
        S[i] = S[i].lower()
print(''.join(S))
