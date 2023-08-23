N = int(input())
dp = [0] * 1000001

dp[2] = 1
dp[3] = 1

for i in range(4, N + 1):
    res = [dp[i - 1] + 1]
    if i % 3 == 0:
        res.append(dp[int(i / 3)] + 1)
    if i % 2 == 0:
        res.append(dp[int(i / 2)] + 1)
    dp[i] = min(res)

print(dp[N])
