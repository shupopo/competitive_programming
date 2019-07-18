A, B, C = map(int, input().split())
K = int(input())

max_num = max([A, B, C])
sum = A + B + C - max_num

for i in range(K):
    max_num *= 2
sum += max_num

print(sum)
