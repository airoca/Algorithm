def blizzard(d,s):
    global n
    if d==1:
        for i in range(1,s+1):
            graph[n//2-i][n//2] = -1
    elif d==2:
        for i in range(1,s+1):
            graph[n//2+i][n//2] = -1
    elif d==3:
        for i in range(1,s+1):
            graph[n//2][n//2-i] = -1
    else:
        for i in range(1,s+1):
            graph[n//2][n//2+i] = -1

    lst = []
    
    size = n-1
    x,y = 0,0
    while size>1:
        for _ in range(size):
            lst.append(graph[x][y])
            y+=1
        for _ in range(size):
            lst.append(graph[x][y])
            x+=1
        for _ in range(size):
            lst.append(graph[x][y])
            y-=1
        for _ in range(size):
            lst.append(graph[x][y])
            x-=1
        x+=1
        y+=1
        size-=2
    lst.append(graph[x][y])
    
    lst = [i for i in lst if i!=-1]
    lst = change(bomb(lst))

    if len(lst)>n**2:
        lst = lst[-n**2:]
    else:
        lst = (n**2-len(lst))*[0] + lst

    size = n-1
    x,y = 0,0
    
    while size>1:
        for _ in range(size):
            graph[x][y] = lst.pop(0)
            y+=1
        for _ in range(size):
            graph[x][y] = lst.pop(0)
            x+=1
        for _ in range(size):
            graph[x][y] = lst.pop(0)
            y-=1
        for _ in range(size):
            graph[x][y] = lst.pop(0)
            x-=1
        x+=1
        y+=1
        size-=2
    graph[x][y] = lst.pop(0)
          
        
def bomb(lst):
    while True:
        to_delete = []
        count = 1
        for i in range(1, len(lst)):
            if lst[i] == lst[i-1]:
                count += 1
                if count == 4:
                    to_delete.append((i-3, i))
                elif count > 4:
                    to_delete[-1] = (to_delete[-1][0], i)
            else:
                count = 1
        if not to_delete:
            break
        for start, end in reversed(to_delete):
            result[lst[start]] += (end-start+1)
            del lst[start:end+1]
    return lst


def change(lst):
    new = []
    start = 0
    count = 1
    for i in range(len(lst) - 1):
        if lst[i]==0:
            continue
        if lst[i] == lst[i + 1]:
            count += 1
        else:
            new.append(lst[i])
            new.append(count)
            start += i + 1
            count = 1
    new.append(0)
    return new
    

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
b = [list(map(int,input().split())) for _ in range(m)]
dx = [0,1,0,-1]
dy = [-1,0,1,0]

result = [0,0,0,0]

for i in b:
    d,s = i
    blizzard(d,s)

print(result[1]+2*result[2]+3*result[3])