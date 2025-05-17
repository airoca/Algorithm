import heapq
INF = int(1e9)

def solution(N, road, K):
    
    answer = 0
    distance = [INF] * (N+1)
    
    graph = [[] for _ in range(N+1)]
    
    for r in road:
        x, y, cost = r[0], r[1], r[2]
        graph[x].append((cost, y))
        graph[y].append((cost, x))
    
    queue = []
    
    start = 1
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        cur_cost, cur_node = heapq.heappop(queue)
        
        if distance[cur_node] < cur_cost:
            continue
        
        for nxt in graph[cur_node]:
            if distance[nxt[1]] > cur_cost + nxt[0]:
                distance[nxt[1]] = cur_cost + nxt[0]
                heapq.heappush(queue,(distance[nxt[1]], nxt[1]))
            
    for d in distance:
        if d <= K:
            answer += 1

    return answer