N = int(input())
S1 = list(input())
S2 = S1.copy()
count1 = 0
count2 = 0
for i in range(0, N-1, 1):
    if S1[i] == "#" and S1[i + 1] == ".":
        S1[i + 1] = "#"
        count1 += 1

for i in range(N-1, 0, -1):
    if S2[i-1] == "#" and S2[i] == ".":
        S2[i-1] = "."
        count2 += 1
print(min(count1, count2))
# print(count2)
# see https://www.python.ambitious-engineer.com/archives/1757
