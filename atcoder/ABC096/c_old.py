H, W = map(int, input().split())

line_list = []

for i in range(H):
    line = input()
    line_list.append(line)

flag = True
print(line_list)
for i in range(len(line_list)):
    for j in range(len(line_list[i])):
        if flag = False:
            break
        if line_list[i][j] == "#":
            if i == 0 and j == 0:
                if "#" not in [line_list[i+1][j], line_list[i][j+1]]:
                    flag = False
            elif i == H - 1 and j == W - 1:
                if "#" not in [line_list[i-1][j], line_list[i][j-1]]:
                    flag = False
            elif i == 0:
                if "#" not in [line_list[i + 1][j], line_list[i][j-1], line_list[i][j + 1]]:
                    flag = False
            elif i == H - 1:
                if "#" not in [line_list[i-1][j], line_list[i][j-1], line_list[i][j + 1]]:
                    flag = False
            elif j == 0:
                if "#" not in [line_list[i - 1][j], line_list[i + 1][j], line_list[i][j + 1]]:
                    flag = False
            elif j == W - 1:
                if "#" not in [line_list[i - 1][j], line_list[i + 1][j], line_list[i][j - 1]]:
                    flag = False
            else:
                if "#" not in [line_list[i - 1][j], line_list[i + 1][j], line_list[i][j - 1], line_list[i][j + 1]]:
                    flag = False
print("Yes" if flag else "No")
