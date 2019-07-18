N, K = map(int, input().split())
S = list(input())

nums = []
now = 1
count = 0
for i in range(len(S)):
    if S[i] is str(now):
        count += 1
    else:
        nums.append(count)
        now = 1 - now
        count = 1
if count != 0:
    nums.append(count)
if len(nums) % 2 == 0:
    nums.append(0)  # ? 1を足すのでは？？

add = 2 * K + 1

sum = [0] * (len(nums)+1)
for i in range(len(nums)):
    sum[i+1] = sum[i] + nums[i]
ans = 0
print(list(range(0,len(nums), 2)))
for i in range(0,len(nums), 2):
    left = i
    right = min(i + add, len(nums))
    tmp = sum[right] - sum[left]
    ans = max(tmp, ans)

print(ans)