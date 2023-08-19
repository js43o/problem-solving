import sys
from collections import deque

input = sys.stdin.readline


def dfs(mat, l, cur_y, cur_x, to_y, to_x, count):
    if cur_y == to_y and cur_x == to_x:
        print(mat[cur_y][cur_x])
        return

    for dy, dx in [
        [-2, -1],
        [-1, -2],
        [1, -2],
        [2, -1],
        [2, 1],
        [1, 2],
        [-1, 2],
        [-2, 1],
    ]:
        if (
            0 <= cur_y + dy < l
            and 0 <= cur_x + dx < l
            and mat[cur_y + dy][cur_x + dx] == 0
        ):
            mat[cur_y + dy][cur_x + dx] = count + 1
            dfs(mat, l, cur_y + dy, cur_x + dx, to_y, to_x, count + 1)


T = int(input())
for _ in range(T):
    l = int(input())
    from_y, from_x = map(int, input().split())
    to_y, to_x = map(int, input().split())

    mat = [[0] * l for _ in range(l)]
    q = deque([[from_y, from_x]])

    while q:
        y, x = q.popleft()
        if y == to_y and x == to_x:
            print(mat[y][x])
            break

        for dy, dx in [
            [-2, -1],
            [-1, -2],
            [1, -2],
            [2, -1],
            [2, 1],
            [1, 2],
            [-1, 2],
            [-2, 1],
        ]:
            if 0 <= y + dy < l and 0 <= x + dx < l and mat[y + dy][x + dx] == 0:
                mat[y + dy][x + dx] = mat[y][x] + 1
                q.append([y + dy, x + dx])
