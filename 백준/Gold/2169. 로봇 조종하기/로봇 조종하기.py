from collections import deque

n, m = map(int, input().split())
graph = []
dp = [[0] * m for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int,input().split())))

dp[0][0] = graph[0][0]

for i in range(1, m):
    dp[0][i] = dp[0][i-1] + graph[0][i]

for col in range(1, n):

    left_dp = [0] * m
    right_dp = [0] * m

    # from left
    for row in range(m):
        if row == 0:
            left_dp[row] = dp[col-1][row] + graph[col][row]
        else:
            left_dp[row] = max(dp[col-1][row], left_dp[row-1]) + graph[col][row]

    # from right
    for row in range(m-1, -1, -1):
        if row == m-1:
            right_dp[row] = dp[col-1][row] + graph[col][row]
        else:
            right_dp[row] = max(dp[col-1][row], right_dp[row+1]) + graph[col][row]

    for i in range(m):
        dp[col][i] = max(left_dp[i], right_dp[i])

print(dp[n-1][m-1])