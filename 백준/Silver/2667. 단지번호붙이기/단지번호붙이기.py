n = int(input())
graph = []
lst = []
result = 0

for _ in range(n):
    graph.append(list(map(int,input())))

def dfs(x, y):
    global numbers
    if x<0 or x>=n or y<0 or y>=n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        numbers += 1
        return True
    return False

for i in range(n):
    for j in range(n):
        numbers = 0
        if dfs(i,j)==True:
            result += 1
            lst.append(numbers)
            
lst.sort()

print(result)

for i in lst:
    print(i)