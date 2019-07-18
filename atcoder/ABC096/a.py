a, b = map(int, input().split())

takahashi = 0

if a <= b:
    takahashi = a
else:
    takahashi = a - 1

print(takahashi)
