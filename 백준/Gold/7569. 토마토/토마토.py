from collections import deque

m,n,h = map(int,input().split())
graph = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]
result = []
d = [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]

queue = deque()

for box in range(h):
    for x in range(n):
        for y in range(m):
            if graph[box][x][y]==1:
                queue.append((box,x,y,1))

result = 1

while queue:
    box, x, y, date = queue.popleft()
    result = date
    for dbox, dx, dy in d:
        nbox = box + dbox
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m or nbox < 0 or nbox >= h:
            continue
        if graph[nbox][nx][ny] == 0:
            graph[nbox][nx][ny] = date+1
            queue.append((nbox,nx,ny,date+1))
            
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