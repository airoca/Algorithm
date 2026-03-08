from collections import deque

def solution(n, wires):
    answer = 100
    graph = [[] for _ in range(n+1)]
    
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    def bfs():
        count = 1
        visited = [False] * (n+1)
        queue = deque()
        queue.append(1)
        visited[1] = True
        while queue:
            cur = queue.popleft()
            for nxt in graph[cur]:
                if not visited[nxt]:
                    visited[nxt] = True
                    queue.append(nxt)
                    count += 1
        return abs(count - (n-count)) 
    
    for i in range (len(wires)):
        v1, v2 = wires[i]
        graph[v1].remove(v2)
        graph[v2].remove(v1)
        temp = bfs()
        answer = min(answer, temp)
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    return answer