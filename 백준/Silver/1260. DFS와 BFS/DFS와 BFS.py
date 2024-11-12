from collections import deque

n,m,v = map(int,input().split())
graph = [[False]*(n+1) for _ in range(n+1)]

for _ in range(m):
    x,y = map(int,input().split())
    graph[x][y] = True
    graph[y][x] = True

visited_dfs = [False]*(n+1)
visited_bfs = [False]*(n+1)

def dfs(v, graph):
    visited_dfs[v] = True
    print(v, end = " ")
    for i in range(1,n+1):
        if graph[v][i] and not visited_dfs[i]:
            dfs(i, graph)

def bfs(v, graph):
    queue = deque([v])
    visited_bfs[v] = True
    while queue:
        v = queue.popleft()
        print(v, end = " ")
        for i in range(1,n+1):
            if graph[v][i] and not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True

dfs(v, graph)
print()
bfs(v, graph)