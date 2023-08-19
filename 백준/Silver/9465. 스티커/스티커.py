import sys

T = int(input())
for _ in range(T):
    N = int(input())
    arr = [(list(map(int, input().split())))]
    arr.append(list(map(int, input().split())))
    dp = [[0] * 2 for _ in range(N)]
    dp[0][0] = arr[0][0]
    dp[0][1] = arr[1][0]
    if N >= 2:
        dp[1][0] = dp[0][1] + arr[0][1]
        dp[1][1] = dp[0][0] + arr[1][1]
    for i in range(2, N):
        dp[i][0] = arr[0][i] + max(dp[i - 1][1], max(dp[i - 2][0], dp[i - 2][1]))
        dp[i][1] = arr[1][i] + max(dp[i - 1][0], max(dp[i - 2][0], dp[i - 2][1]))
    print(max(dp[N - 1][0], dp[N - 1][1]))
