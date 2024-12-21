n,k = map(int,input().split())
lst = [int(input()) for _ in range(n)]
dp = [0]*(k+1)

dp[0] = 1

for coin in lst:
    for i in range(coin,k+1):
        dp[i] = dp[i] + dp[i-coin]

print(dp[k])