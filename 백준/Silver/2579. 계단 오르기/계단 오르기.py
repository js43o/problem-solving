import sys

N = int(input())
stair = [0]
for _ in range(N):
    stair.append(int(sys.stdin.readline().rstrip()))

if N == 1:
    print(stair[1])
elif N == 2:
    print(stair[1] + stair[2])
else:
    dp = [0] * 999

    dp[1] = stair[1]
    dp[2] = stair[1] + stair[2]

    for i in range(3, N + 1):
        dp[i] = max(dp[i - 3] + stair[i - 1] + stair[i], dp[i - 2] + stair[i])

    print(dp[N])
