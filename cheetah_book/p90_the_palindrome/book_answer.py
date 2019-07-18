s = list(input())

for i in range(len(s), 2 * len(s)):
    flag = True
    for j in range(len(s)):
        if i - j - 1 < len(s) and s[j] != s[i - j - 1]:
            flag = False
            break
    if flag:
        print(i)
        break
