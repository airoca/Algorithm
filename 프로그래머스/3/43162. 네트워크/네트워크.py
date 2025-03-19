def solution(n, computers):
    answer = 0
    visited = [False] * n
    for s in range(n):
        if visited[s] == False:
            dfs(n, s, computers, visited)
            answer += 1
    return answer

def dfs(n, s, computers, visited):
    visited[s] = True
    for i in range(n):
        if computers[s][i] == 1 and visited[i] == False:
            visited[i] = True
            dfs(n, i, computers, visited)
    return True