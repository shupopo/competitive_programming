def main():
    friends = ["NYNNN", "YNYNN", "NYNYN", "NNYNY", "NNNYN"]
    n = len(friends[0])
    ans = 0
    for i in range(n):
        count = 0
        for j in range(n):
            if i == j:
                continue
            if friends[i][j] == "Y":
                count += 1
            else:
                for k in range(n):
                    if friends[j][k] == "Y" and friends[k][i] == "Y":
                        count += 1
                        break
        ans = max(ans, count)
    print(ans)


if __name__ == '__main__':
    main()

# pythonでjavaのcharatに相当するメソッドはなにか
# https://www.quora.com/What-is-the-Python-equivalent-to-Javas-charat-method
