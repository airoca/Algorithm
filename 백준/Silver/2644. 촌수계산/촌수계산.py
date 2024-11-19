from collections import deque

n = int(input())
x,y = map(int,input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(v):
    queue = deque([(v, 0)])

    while queue:
        v,chon = queue.popleft()
        
        if v==y:
            return chon
        
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append((i, chon+1))

    return -1

print(bfs(x))