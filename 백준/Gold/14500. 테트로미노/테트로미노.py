import sys

input = sys.stdin.readline

N, M = map(int, input().split())
matrix = []
visited = [[False] * M for _ in range(N)]
result = 0

for _ in range(N):
    matrix.append(list(map(int, input().split())))


def dfs(y, x, sum, count):
    global result

    if count >= 4:
        result = max(result, sum)
        return

    for dy, dx in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        if 0 <= y + dy < N and 0 <= x + dx < M and not visited[y + dy][x + dx]:
            visited[y + dy][x + dx] = True
            dfs(y + dy, x + dx, sum + matrix[y + dy][x + dx], count + 1)
            visited[y + dy][x + dx] = False


def fuq(y, x):
    global result

    up = [(-1, 0), (0, -1), (0, 1)]
    left = [(-1, 0), (1, 0), (0, 1)]
    bottom = [(1, 0), (0, -1), (0, 1)]
    right = [(-1, 0), (1, 0), (0, -1)]

    for direction in [up, left, bottom, right]:
        (y1, x1), (y2, x2), (y3, x3) = direction
        if (
            0 <= y + y1 < N
            and 0 <= y + y2 < N
            and 0 <= y + y3 < N
            and 0 <= x + x1 < M
            and 0 <= x + x2 < M
            and 0 <= x + x3 < M
        ):
            result = max(
                result,
                matrix[y][x]
                + matrix[y + y1][x + x1]
                + matrix[y + y2][x + x2]
                + matrix[y + y3][x + x3],
            )


for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, matrix[i][j], 1)
        visited[i][j] = False
        fuq(i, j)

print(result)
