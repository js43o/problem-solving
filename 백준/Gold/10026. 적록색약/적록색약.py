import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
matrix_o, matrix_g = [], []

for _ in range(N):
    str = input().rstrip()
    matrix_o.append(list(str))
    matrix_g.append(list(str.replace("G", "R")))


def bfs(i, j, matrix):
    q = deque([(i, j)])
    color = matrix[i][j]
    matrix[i][j] = "X"

    while q:
        y, x = q.popleft()

        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= y + dy < N and 0 <= x + dx < N and matrix[y + dy][x + dx] == color:
                q.append((y + dy, x + dx))
                matrix[y + dy][x + dx] = "X"


count_o, count_g = 0, 0

for i in range(N):
    for j in range(N):
        if matrix_o[i][j] != "X":
            bfs(i, j, matrix_o)
            count_o += 1
        if matrix_g[i][j] != "X":
            bfs(i, j, matrix_g)
            count_g += 1

print(count_o)
print(count_g)
