import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input().rstrip())
M = int(input().rstrip())
INF = 10**9
graph = [[INF] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b, r = map(int, input().split())
    if r < graph[a][b]:
        graph[a][b] = r

for i in range(N + 1):
    graph[i][i] = 0

for x in range(N + 1):
    for y in range(N + 1):
        for k in range(N + 1):
            if graph[y][x] + graph[x][k] < graph[y][k]:
                graph[y][k] = graph[y][x] + graph[x][k]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if graph[i][j] == INF:
            graph[i][j] = 0
    print(*graph[i][1:])
