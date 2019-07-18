N = int(input())
dishes = [int(input()) for _ in range(N)]
dishes.reverse()
for i in range(N):
    if dishes[i] > dishes[i + 1]:
        print(dishes[i + 1])
        break
    else:
        continue
