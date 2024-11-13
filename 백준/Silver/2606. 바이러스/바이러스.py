n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
result = 0

for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(cur):
    global result
    visited[cur] = True
    result+=1
    for i in graph[cur]:
        if not visited[i]:
            dfs(i)

dfs(1)
print(result-1)