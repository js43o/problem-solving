import sys

T = int(input())
dp = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
dp.extend([0] * 90)

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    if (N <= 10):
      print(dp[N])
      continue
    for i in range(11, N + 1):
      dp[i] = dp[i - 1] + dp[i - 5]
    print(dp[N])