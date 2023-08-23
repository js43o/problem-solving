import sys

input = sys.stdin.readline

N = int(input())
costs = []
res = 10**9

for _ in range(N):
    arr = list(map(int, input().split()))
    costs.append(arr)

for i in range(3):
    dp = [[0] * 3 for _ in range(N)]  # dp[n][k] == n번째 집을 인덱스 k의 색으로 칠했을 때까지의 최소 비용
    rests = list(filter(lambda n: n != i, [0, 1, 2]))  # 첫 번째 집의 색을 제외한 색 인덱스
    dp[1][i] = 10**9  # 두 번째 집에서 제외할 색 (첫 번째 집에 먼저 칠한 색)
    for j in rests:
        dp[1][j] = costs[0][i] + costs[1][j]  # 두 번째 집까지의 비용을 먼저 계산

    for k in range(2, N):
        for cur, prev1, prev2 in [(0, 1, 2), (1, 0, 2), (2, 0, 1)]:
            dp[k][cur] = min(dp[k - 1][prev1], dp[k - 1][prev2]) + costs[k][cur]

    for i in rests:
        res = min(res, dp[N - 1][i])

print(res)
