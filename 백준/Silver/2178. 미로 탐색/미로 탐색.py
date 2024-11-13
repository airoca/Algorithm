from collections import deque

n,m = map(int,input().split())
graph = [list(map(int,input())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

queue = deque()
queue.append([0,0,1])
visited[0][0] = True

while queue:
    x,y,d = queue.popleft()
    if x==n-1 and y==m-1:
        print(d)
        break
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] and not visited[nx][ny]:
                queue.append([nx,ny,d+1])
                visited[nx][ny] = True