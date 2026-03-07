from collections import deque

start, dest = map(int, input().split())
INF = int(1e9)
dist = [INF] * 100001
dq = deque()
dq.append(start)
dist[start] = 0

while dq:
    cur = dq.popleft()
    for nxt, cost in [(cur*2,0),(cur-1,1),(cur+1,1)]:
        if 0 <= nxt <= 100000 and dist[nxt] > dist[cur]+cost:
            dist[nxt] = dist[cur]+cost
            if cost==0:
                dq.appendleft(nxt)
            else:
                dq.append(nxt)
print(dist[dest])