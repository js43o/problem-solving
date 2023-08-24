import sys
import heapq

input = sys.stdin.readline

N = int(input())
dp = [[0] * 10 for _ in range(N)]
mod = 1000000000
res = 0

for k in range(1, 10):  # 0은 제외하고
    dp[0][k] = 1  # 초기 경우의 수는 1

for i in range(1, N):
    for k in range(10):  # 0~9
        if k - 1 >= 0:
            dp[i][k] += dp[i - 1][k - 1]
        if k + 1 <= 9:
            dp[i][k] += dp[i - 1][k + 1]
        dp[i][k] %= mod

for k in range(10):
    res += dp[N - 1][k]
    res %= mod

print(res)
