l = [""] * 4

for i in range(4):
    l[i] = input()
for i in reversed(l):
    print("".join(list(reversed(i))))
