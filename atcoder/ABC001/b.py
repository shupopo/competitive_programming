m = int(input())
k = 1000

if m < 0.1 * k:
    print("00")
elif m <= 5 * k:
    result = str(m // 100)
    if len(result) == 1:
        print("0" + result)
    else:
        print(result)
elif 6 * k <= m and m <= 30 * k:
    print(m // k + 50)
elif 35 * k <= m and m <= 70 * k:
    print((m // k - 30) // 5 + 80)
elif 70 * k < m:
    print(89)
