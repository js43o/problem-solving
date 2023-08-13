import sys

input = sys.stdin.readline
INF = 1e9


def dfs(v, visited, N, dist, dp):
    if visited == (1 << N) - 1:
        if dist[v][0]:
            return dist[v][0]
        return INF

    if dp[v][visited] != -1:
        return dp[v][visited]

    dp[v][visited] = INF
    for w in range(N):
        if v == w or dist[v][w] == 0 or visited & (1 << w):
            continue

        minCost = dfs(w, visited | (1 << w), N, dist, dp) + dist[v][w]
        if minCost < dp[v][visited]:
            dp[v][visited] = minCost

    return dp[v][visited]


N = int(input())
dist = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1] * (1 << N) for _ in range(N)]
print(dfs(0, 1, N, dist, dp))
