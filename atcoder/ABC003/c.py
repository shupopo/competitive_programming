
N, K = map(int, input().split())
# 小さい順位レートをソート
# 小さい方からN-K除去
# 残ったうち小さい方からK個見ればよい

rates = [int(i) for i in input().split()]
rates.sort()
if N-K > 0:
    del rates[0:N - K]
ans = 0
for rate in rates:
    ans = (ans + rate) / 2
print(ans)
