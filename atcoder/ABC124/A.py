A,B=map(int,input().split())
coins = 0
for i in range(2):
    if A > B:
        coins += A
        A -= 1
    else:
        coins += B
        B -= 1
print(coins)