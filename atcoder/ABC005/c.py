T = int(input())
N = int(input())
takoyaki_list = list(map(int, input().split()))
M = int(input())
customer_list = list(map(int, input().split()))
# [int(x) for x in input().split()]

sold_flags = [False] * N
bought_flags = []

if N < M:
    bought_flags.append(False)
else:
    for i in range(M):
        bought_flag = False
        bought_flags.append(bought_flag)
        for j in range(N):
            # customer_list[i] > takoyaki_list[j]としてハマった
            # たこやきができるのと同時に客が来てもOK
            if sold_flags[j] == False and customer_list[i] >= takoyaki_list[j] and customer_list[i] - takoyaki_list[j] <= T:
                sold_flags[j] = True
                bought_flags[i] = True
                break

print("yes" if False not in bought_flags else "no")

# https://atcoder.jp/contests/abc005/submissions/5875307
# n, mの関係を捉えるときは、O(n^2)になりがち
# n, mが小さいから通るが、本来ならTLE
# n, mが出てくるときは、尺取法の方針で