numbers = [1, 1, 1, 1]
ans = 0

for i in range(len(numbers)):
    numbers[i] += 1
    result = 1
    for num in numbers:
        result *= num
    ans = max(result, ans)
    numbers[i] -= 1
print(ans)
