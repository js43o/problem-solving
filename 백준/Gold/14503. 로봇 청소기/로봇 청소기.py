import sys

input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
mat = []
res = 0


def existsUncleaned(y, x):
    for dy, dx in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        if 0 <= y + dy < N and 0 <= x + dx < M and mat[y + dy][x + dx] == 0:
            return True

    return False


def goBack(dir):
    if dir == 0:
        return [1, 0]
    if dir == 1:
        return [0, -1]
    if dir == 2:
        return [-1, 0]
    if dir == 3:
        return [0, 1]
    return None


def goForward(dir):
    dy, dx = goBack(dir)
    return [-dy, -dx]


for _ in range(N):
    arr = list(map(int, input().split()))
    mat.append(arr)

while True:
    if mat[r][c] == 0:
        mat[r][c] = -1  # 방문 표시
        res += 1

    if existsUncleaned(r, c):
        d = (d - 1) % 4
        dy, dx = goForward(d)
        if 0 <= r + dy < N and 0 <= c + dx < M and mat[r + dy][c + dx] == 0:
            r += dy
            c += dx
        continue

    dy, dx = goBack(d)
    if 0 <= r + dy < N and 0 <= c + dx < M and mat[r + dy][c + dx] != 1:
        r += dy
        c += dx
    else:
        break


print(res)
