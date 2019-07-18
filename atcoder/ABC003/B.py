S = list(input())
T = list(input())
flag = True
for i in range(len(S)):
    if S[i] == T[i]:
        continue
    elif S[i] == "@":
        if T[i] in ["a", "t", "c", "o", "d", "e", "r"]:
            continue
        else:
            flag = False
            break
    elif T[i] == "@":
        if S[i] in ["a", "t", "c", "o", "d", "e", "r"]:
            continue
        else:
            flag = False
            break
    else:
        flag = False
        break
if flag:
    print("You can win")
else:
    print("You will lose")
