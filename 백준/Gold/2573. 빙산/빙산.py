from collections import deque

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x, y):
    queue = deque([(x,y)])
    visited[x][y] = True
    seaList = []

    while queue:
        x,y = queue.popleft()
        sea = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if not graph[nx][ny]:
                sea += 1
            elif not visited[nx][ny]:
                queue.append((nx,ny))
                visited[nx][ny] = True
        if sea > 0:
            seaList.append((x,y,sea))
    for x,y,sea in seaList:
        graph[x][y] = max(0, graph[x][y] - sea)

    return 1

result = 0

ice = []
for i in range(n):
    for j in range(m):
        if graph[i][j]:
            ice.append((i,j))

while ice:
    visited = [[False]*m for _ in range(n)]
    melted = []
    group = 0

    for i, j in ice:
        if not visited[i][j]:
            group += bfs(i,j)
        if graph[i][j] == 0:
            melted.append((i,j))

    if group > 1:
        print(result)
        break

    ice = [x for x in ice if x not in melted]
    result += 1

if group < 2:
    print(0)