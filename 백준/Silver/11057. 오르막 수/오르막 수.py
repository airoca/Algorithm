n = int(input())
dp = [1]*10

for _ in range(n):
    for i in range(1,10):
        dp[i] += dp[i-1]

print(dp[-1]%10007)