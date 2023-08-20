import sys

input = sys.stdin.readline

N, M = map(int, input().split())
mems = [0] + list(map(int, input().split()))
costs = [0] + list(map(int, input().split()))
dp = [[0] * (N + 1) for _ in range(10001)]  # dp[앱 인덱스][비용] = 확보된 메모리

for totalCost in range(10001):
    for idx in range(1, N + 1):
        if costs[idx] > totalCost:
            dp[totalCost][idx] = dp[totalCost][idx - 1]
            continue
        dp[totalCost][idx] = max(
            dp[totalCost][idx - 1], dp[totalCost - costs[idx]][idx - 1] + mems[idx]
        )

        if dp[totalCost][idx] >= M:
            print(totalCost)
            exit(0)
