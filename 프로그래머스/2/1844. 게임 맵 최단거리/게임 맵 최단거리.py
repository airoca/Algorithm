from collections import deque

def solution(maps):
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    
    queue = deque()
    queue.append((0,0,1))
    visited[0][0] = True
    
    while queue:
        x,y,cost = queue.popleft()
        
        if x==n-1 and y==m-1:
            return cost
    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if maps[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append([nx,ny,cost+1])
    
    return -1