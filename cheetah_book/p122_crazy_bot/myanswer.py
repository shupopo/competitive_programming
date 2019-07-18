import sys
sys.setrecursionlimit(100000)

n = int(input())
east = int(input())
west = int(input())
south = int(input())
north = int(input())

ans = 0

count = [0, 0, 0, 0]

now = [0, 0]

positions = []


def dfs(now, count, positions, n):
    print(positions)
    if sum(count) < n and now in positions:
        return 0
    positions.append(now)
    for direction in ["e", "w", "s", "n"]:
        next = [0, 0]
        if direction == "e":
            next = [now[0] + 1, now[1]]
            count[0] += 1
        elif direction == "w":
            next = [now[0] - 1, now[1]]
            count[1] += 1
        elif direction == "s":
            next = [now[0], now[1] - 1]
            count[2] += 1
        elif direction == "n":
            next[now[0], now[1]+1]
            count[3] += 1
        count = dfs(next, count, positions, n)
    if sum(count) == n and now not in positions:
        return count
    elif sum(count) == n and now in positions:
        return 0


result = dfs([0, 0], [0, 0, 0, 0], [], n)
print(result)
