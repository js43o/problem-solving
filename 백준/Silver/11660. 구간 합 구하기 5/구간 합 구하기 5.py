import sys

input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [[0] * (N + 1)]

for i in range(N):
    arr = list(map(int, input().split()))
    matrix.append([0] + arr)

for y in range(N + 1):
    for x in range(1, N + 1):
        matrix[y][x] += matrix[y][x - 1]

for x in range(N + 1):
    for y in range(1, N + 1):
        matrix[y][x] += matrix[y - 1][x]


for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = (
        matrix[x2][y2]
        - matrix[x2][y1 - 1]
        - matrix[x1 - 1][y2]
        + matrix[x1 - 1][y1 - 1]
    )
    print(result)
