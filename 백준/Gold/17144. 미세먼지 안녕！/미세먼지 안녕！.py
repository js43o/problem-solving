import sys
from copy import deepcopy
from collections import deque
from itertools import combinations, chain

input = sys.stdin.readline

R, C, T = map(int, input().split())
matrix = []
purifier = []

for i in range(R):
    matrix.append(list(map(int, input().split())))
    if matrix[i][0] == -1:
        purifier.append((i))


def bfs(matrix):
    q = deque()
    adder = [[0] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if matrix[i][j] > 0:
                q.append((i, j))

    while q:
        i, j = q.popleft()
        v = matrix[i][j] // 5
        for dy, dx in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            if 0 <= i + dy < R and 0 <= j + dx < C and matrix[i + dy][j + dx] != -1:
                adder[i + dy][j + dx] += v
                matrix[i][j] -= v

    for i in range(R):
        for j in range(C):
            if matrix[i][j] == -1:
                continue
            matrix[i][j] += adder[i][j]

    circulate(matrix, "top", purifier[0])
    circulate(matrix, "bottom", purifier[1])

    return matrix


def circulate(matrix, direction, Y):
    if direction == "top":
        for i in range(Y, 0, -1):
            matrix[i][0] = matrix[i - 1][0]
        for j in range(0, C - 1):
            matrix[0][j] = matrix[0][j + 1]
        for i in range(0, Y):
            matrix[i][C - 1] = matrix[i + 1][C - 1]
        for j in range(C - 1, 1, -1):
            matrix[Y][j] = matrix[Y][j - 1]
        matrix[Y][1] = 0
    else:
        for i in range(Y, R - 1):
            matrix[i][0] = matrix[i + 1][0]
        for j in range(0, C - 1):
            matrix[R - 1][j] = matrix[R - 1][j + 1]
        for i in range(R - 1, Y, -1):
            matrix[i][C - 1] = matrix[i - 1][C - 1]
        for j in range(C - 1, 1, -1):
            matrix[Y][j] = matrix[Y][j - 1]
        matrix[Y][1] = 0
    matrix[Y][0] = -1


for _ in range(T):
    matrix = bfs(matrix)
result = [x for x in list(chain(*matrix)) if x > 0]
print(sum(result))
