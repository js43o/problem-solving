import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**9)

N, K = map(int, input().split())
d = [[0] * (K + 1) for _ in range(N + 1)]
items = [(0, 0)]
for _ in range(N):
    W, V = map(int, input().split())
    items.append((W, V))

for i in range(1, N + 1):
    for j in range(1, K + 1):
        w, v = items[i]
        if j < w:
            d[i][j] = d[i - 1][j]
        else:
            d[i][j] = max(d[i - 1][j - w] + v, d[i - 1][j])

print(d[N][K])
