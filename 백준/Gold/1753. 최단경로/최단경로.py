import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

v,e = map(int,input().split())
start = int(input())

heap = []
graph = [[] for _ in range(v+1)]

for i in range(e):
    from_node, dest_node, weight = map(int,input().split())
    graph[from_node].append((dest_node,weight))

def dijkstra(start):
    distance = [INF] * (v+1)
    distance[start] = 0
    heap = []
    heapq.heappush(heap,(0,start))

    while heap:
        current_dist, current_node = heapq.heappop(heap)

        if distance[current_node] < current_dist:
            continue

        for next_node, weight in graph[current_node]:
            if current_dist + weight < distance[next_node]:
                distance[next_node] = current_dist + weight
                heapq.heappush(heap, (distance[next_node], next_node))

    return distance

distance = dijkstra(start)

for i in range(1,v+1):
    if (distance[i] == INF):
        print("INF")
    else:
        print(distance[i])
