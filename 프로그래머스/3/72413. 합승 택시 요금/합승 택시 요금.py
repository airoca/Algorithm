import heapq

def solution(n, s, a, b, fares):
    answer = 0
    graph = [[] for _ in range(n + 1)]
    for u, v, w in fares:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # s, a, b 각각에서의 최단거리 테이블
    dist_from_s = dijkstra(s, n, graph)
    dist_from_a = dijkstra(a, n, graph)
    dist_from_b = dijkstra(b, n, graph)
    
    # 가능한 모든 합승 분기점 k에 대해 최소 요금 계산
    answer = float('inf')
    for k in range(1, n + 1):
        cost = dist_from_s[k] + dist_from_a[k] + dist_from_b[k]
        answer = min(answer, cost)
    
    return answer

def dijkstra(s, n, graph):
    INF = 10 ** 9
    distance = [INF] * (n+1)
    distance[s] = 0
    queue = [(0, s)]
    
    while queue:
        dist, now = heapq.heappop(queue)
        if dist > distance[now]:
            continue
        for nxt, cost in graph[now]:
            if dist + cost < distance[nxt]:
                distance[nxt] = dist + cost
                heapq.heappush(queue, (dist + cost, nxt))
    
    return distance

