import math

N = int(input())
Z = math.floor(math.sqrt(N))
dp = [0] * (N + 1)

dp[0] = 0
dp[1] = 1

for i in range(2, N + 1):
    arr = []
    for j in range(1, math.floor(math.sqrt(i)) + 1):
        arr.append(dp[i - j ** 2] + 1)
    dp[i] = min(arr)

print(dp[N])
