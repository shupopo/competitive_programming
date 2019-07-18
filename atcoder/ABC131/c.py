A, B, C, D = map(int, input().split())
count = 0

for num in range(A, B + 1):
    if num % C == 0 or num % D == 0:
        continue
    else:
        count += 1

print(count)
