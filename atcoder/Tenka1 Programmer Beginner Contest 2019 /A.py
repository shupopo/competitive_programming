A, B, C = map(int, input().split())
ans = "No"

if A <= C and C <= B:
    ans = "Yes"
if B <= C and C <= A:
    ans = "Yes"
print(ans)