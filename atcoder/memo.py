N = int(input())
nums = [int(input()) for _ in range(N)]
ans = "Yes"
for i in range(len(nums)):
    if i == 0:
        if bin(nums[N-1]^nums[1])==bin(nums[0]):
            continue
        else:
            ans = "No"
    elif i == N-1:
        if bin(nums[N-2]^nums[0])==bin(nums[N-1]):
            continue
        else:
            ans = "No"
    else:
        if bin(nums[i-1]^nums[i+1])==bin(nums[i]):
            continue
        else:
            ans = "No"

print(ans)
