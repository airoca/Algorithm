from collections import deque

m,n,h = map(int,input().split())
graph = [[] for _ in range(h)]
result = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]
dbox = [1,-1]

for box in range(h):
    for _ in range(n):
        graph[box].append(list(map(int,input().split())))

queue = deque()

for box in range(h):
    for x in range(n):
        for y in range(m):
            if graph[box][x][y]==1:
                queue.append([box,x,y,1])

result = 1

while queue:
    box, x, y, date = queue.popleft()
    result = date
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if graph[box][nx][ny] == 0:
            graph[box][nx][ny] = date+1
            queue.append([box,nx,ny,date+1])
    for i in range(2):
        nbox = box + dbox[i]
        if nbox < 0 or nbox >= h:
            continue
        if graph[nbox][x][y] == 0:
            graph[nbox][x][y] = date+1
            queue.append([nbox,x,y,date+1])

success = True

for box in range(h):
    for x in range(n):
        for y in range(m):
            if graph[box][x][y]==0:
                success = False

if success:
    print(result-1)
else:
    print(-1)