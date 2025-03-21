import sys, heapq

input = sys.stdin.readline

v,e = map(int,input().split())
root = int(input())
graph = [[] for _ in range(v+1)]
distance = [1e9] * (v+1)
visited = [False] * (v+1)

for _ in range(e):
    start,end,weight = map(int,input().split())
    graph[start].append((end, weight))

def dijkstra(root):
    queue = []
    heapq.heappush(queue, (0,root))
    distance[root] = 0

    while queue:
        weight, cur = heapq.heappop(queue)

        if visited[cur]:
            continue

        visited[cur] = True

        for nxt in graph[cur]:
            if distance[nxt[0]] > weight + nxt[1]:
                distance[nxt[0]] = weight + nxt[1]
                heapq.heappush(queue, (distance[nxt[0]], nxt[0]))

dijkstra(root)

for i in range(1,v+1):
    if distance[i] == 1e9:
        print("INF")
    else:
        print(distance[i])
