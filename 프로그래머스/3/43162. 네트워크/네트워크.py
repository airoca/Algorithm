def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if visited[i] == False:
            dfs(i, visited, computers, n)
            answer += 1
    return answer
    
def dfs(i, visited, computers, n):
    visited[i] = True
    for j in range(n):
        if computers[i][j] == 1 and visited[j] == False:
            dfs(j, visited, computers, n)