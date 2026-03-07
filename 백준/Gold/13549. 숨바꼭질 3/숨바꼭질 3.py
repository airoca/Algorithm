from collections import deque
import sys

input = sys.stdin.readline
INF = 1000000

start, dest = map(int, input().split())
costs = [INF] * 100001
queue = deque()
queue.append([start, 0])
costs[start] = 0

while queue:
    cur, cost = queue.popleft()

    for nxt in [cur+1, cur-1, cur*2]:
        if nxt < 0 or nxt > 100000:
            continue
        if nxt == cur*2 and costs[nxt] > cost:
            costs[nxt] = cost
            queue.append([nxt, cost])
        elif costs[nxt] > cost+1:
            costs[nxt] = cost + 1
            queue.append([nxt, cost+1])


print(costs[dest])