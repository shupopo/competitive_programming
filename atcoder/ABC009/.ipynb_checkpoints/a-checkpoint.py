N = int(input())
ans = 0

if N == 1:
    ans = 1
elif N % 2 == 0:
    ans = N // 2
else:
    ans = N//2+1
print(ans)
