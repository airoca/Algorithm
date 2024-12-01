import copy
import sys

sys.setrecursionlimit(10**6)

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
result_list = []

def dfs(temp, x, y, h):
    if x<0 or x>=n or y<0 or y>=n:
        return False
    if temp[x][y] > h:
        temp[x][y] = 0
        dfs(temp, x+1, y, h)
        dfs(temp, x-1, y, h)
        dfs(temp, x, y+1, h)
        dfs(temp, x, y-1, h)
        return True
    return False

max_value = max(map(max,graph))

for h in range(max_value):
    temp = copy.deepcopy(graph)
    result = 0
    for i in range(n):
        for j in range(n):
            if dfs(temp, i, j, h):
                result += 1
    result_list.append(result)

print(max(result_list))