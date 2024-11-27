from collections import deque

f,s,g,u,d = map(int,input().split())
visited = [False]*(f+1)
d = [u, -d]

queue = deque([(s,0)])
visited[s] = True

flag = False

while queue:
    cur, count = queue.popleft()
    if cur==g:
        flag = True
        print(count)
        break
    for i in range(2):
        ncur = cur+d[i]
        if ncur < 1 or ncur > f or visited[ncur]:
            continue
        else:
            queue.append((ncur,count+1))
            visited[ncur] = True

if not flag:
    print("use the stairs")