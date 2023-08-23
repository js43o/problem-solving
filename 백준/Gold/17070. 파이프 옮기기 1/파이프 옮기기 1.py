import sys
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())
dist = [
    [[0] * 3 for _ in range(N + 1)] for __ in range(N + 1)
]  # 가로 = 0, 세로 = 1, 대각선 = 2
matrix = [[0] * (N + 1)]
for _ in range(N):
    matrix.append([0] + list(map(int, input().split())))

dist[1][2][0] = 1  # (1, 1)의 가로(0)
for i in range(3, N + 1):
    if matrix[1][i] == 0:
        dist[1][i][0] = dist[1][i - 1][0]

for i in range(1, N + 1):
    for j in range(3, N + 1):
        if matrix[i][j] == 0 and matrix[i - 1][j] == 0 and matrix[i][j - 1] == 0:
            dist[i][j][2] = (
                dist[i - 1][j - 1][1] + dist[i - 1][j - 1][0] + dist[i - 1][j - 1][2]
            )
        if matrix[i][j] == 0:
            dist[i][j][0] = dist[i][j - 1][0] + dist[i][j - 1][2]
            dist[i][j][1] = dist[i - 1][j][1] + dist[i - 1][j][2]

print(dist[N][N][0] + dist[N][N][1] + dist[N][N][2])
