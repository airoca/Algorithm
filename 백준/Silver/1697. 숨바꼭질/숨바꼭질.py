from collections import deque

n,k = map(int,input().split())
visited = [False]*100001

queue = deque([(n,0)])

while queue:
    cur, time = queue.popleft()
    if cur == k:
        print(time)
        break
    d = [cur+1, cur-1, cur*2]
    for ncur in d:
        if ncur<0 or ncur>100000 or visited[ncur]:
            continue
        visited[ncur] = True
        queue.append((ncur,time+1))