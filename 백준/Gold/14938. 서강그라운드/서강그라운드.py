import sys

input = sys.stdin.readline
INF = int(1e9)

N, M, R = map(int, input().split())
item = list(map(int, input().split()))
matrix = [[INF] * N for _ in range(N)]

for _ in range(R):
    a, b, l = map(int, input().split())
    matrix[a - 1][b - 1] = min(matrix[a - 1][b - 1], l)
    matrix[b - 1][a - 1] = min(matrix[b - 1][a - 1], l)


for i in range(N):
    for j in range(N):
        for k in range(N):
            matrix[j][k] = min(matrix[j][k], matrix[j][i] + matrix[i][k])
            if j == k:
                matrix[j][k] = 0

result = 0

for i in range(N):
    temp = 0
    for j in range(N):
        if matrix[i][j] <= M:
            temp += item[j]

    result = max(result, temp)


print(result)
