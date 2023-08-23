import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
k = int(input().rstrip())

matrix = [[0] * m for _ in range(n)]
for _ in range(k):
    i, j = map(int, input().split())
    matrix[i - 1][j - 1] = -1


def go(y, x, count):
    if x % 2 == 0:
        if 0 <= y - 1 and x + 1 < m and matrix[y - 1][x + 1] >= 0:
            matrix[y - 1][x + 1] += count
        if x + 1 < m and matrix[y][x + 1] >= 0:
            matrix[y][x + 1] += count
        if y + 1 < n and matrix[y + 1][x] >= 0:
            matrix[y + 1][x] += count
    else:
        if y + 1 < n and x + 1 < m and matrix[y + 1][x + 1] >= 0:
            matrix[y + 1][x + 1] += count
        if x + 1 < m and matrix[y][x + 1] >= 0:
            matrix[y][x + 1] += count
        if y + 1 < n and matrix[y + 1][x] >= 0:
            matrix[y + 1][x] += count


matrix[0][0] = 1
for j in range(m):
    for i in range(n):
        if matrix[i][j] >= 0:
            matrix[i][j] %= 10**9 + 7
            go(i, j, matrix[i][j])

print(matrix[n - 1][m - 1])
