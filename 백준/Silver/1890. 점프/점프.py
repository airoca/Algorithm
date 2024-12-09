n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0 and dp[i][j] != 0:
            k = graph[i][j]
            if i + k < n:
                dp[i + k][j] += dp[i][j]  # 행 이동
            if j + k < n:
                dp[i][j + k] += dp[i][j]  # 열 이동

print(dp[n - 1][n - 1])