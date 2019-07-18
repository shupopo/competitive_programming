N, M = map(int, input().split())

r = range(0, 10**5)
x, y, z = 0, 0, 0
for y in r:
    for z in r:
        if y + 2 * z == M - 2 * N:
            break
    else:
        continue
    break
x = N - (y + z)
if x < 0:
    print("-1 -1 -1")
else:
    print(str(x)+" "+str(y)+" "+str(z))

"""
質問の一次不定方程式の一組の整数解をPythonで求めてみた。
http://rsc.hatenablog.com/entry/20150421/1429565155
"""
