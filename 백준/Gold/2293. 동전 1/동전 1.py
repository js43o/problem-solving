import sys

input = sys.stdin.readline

n, k = map(int, input().split())
dp = [0] * (k + 1)
coin = []

for _ in range(n):
    coin.append(int(input()))

dp[0] = 1
for i in range(n):
    for j in range(k + 1):
        dp[j] += dp[j - coin[i]] if j >= coin[i] else 0

print(dp[k])
