import queue
R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
maze = [input() for _ in range(R)]

q = queue.Queue()
count = 0
current = [sy, sx]
maze[current[0]][current[1]] = str(count)
q.put(current)
while current != [gy, gx]:
    count += 1
    current = q.get()
    foursides = [maze[current[0]+1][current[1]],
                 maze[current[0]-1][current[1]],
                 maze[current[0]][current[1]+1],
                 maze[current[0]][current[1]-1]]
    for side in foursides:
        if side == ".":
            side = "ok"
