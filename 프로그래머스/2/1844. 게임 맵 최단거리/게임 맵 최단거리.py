from collections import deque

def solution(maps):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    row = len(maps[0])
    col = len(maps)
    
    queue = deque([])
    queue.append((0,0,1))
    
    while queue:
        x,y,cost = queue.popleft()
        
        if x == col-1 and y == row-1:
            return cost
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= col or ny < 0 or ny >= row:
                continue
            
            if maps[nx][ny] == 1:
                maps[nx][ny] = cost+1
                queue.append((nx,ny,cost+1))
                
    return -1