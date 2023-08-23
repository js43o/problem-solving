import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())
board = []
visited = [False] * 26
start = (0, 0)
res = 0

for i in range(R):
    s = input().rstrip()
    board.append(list(s))


def dfs(v, count):
    global res, visited

    y, x = v
    res = max(res, count)

    if count == 26:
        return

    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if not (0 <= y + dy < R and 0 <= x + dx < C):
            continue
        if visited[ord(board[y + dy][x + dx]) - ord("A")]:
            continue
        visited[ord(board[y + dy][x + dx]) - ord("A")] = True
        dfs((y + dy, x + dx), count + 1)
        visited[ord(board[y + dy][x + dx]) - ord("A")] = False


visited[ord(board[start[0]][start[1]]) - ord("A")] = True
dfs(start, 1)
print(res)
