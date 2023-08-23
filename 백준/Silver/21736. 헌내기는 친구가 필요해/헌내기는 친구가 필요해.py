import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
visited = [[False] * M for _ in range(N)]
mat = []
start = None
res = 0

for i in range(N):
    s = input().rstrip()
    mat.append(list(s))
    if "I" in s:
        start = (i, s.index("I"))

q = deque([start])
visited[start[0]][start[1]] = True

while q:
    y, x = q.popleft()
    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if not (0 <= y + dy < N and 0 <= x + dx < M):
            continue
        if visited[y + dy][x + dx] or mat[y + dy][x + dx] == "X":
            continue
        visited[y + dy][x + dx] = True
        q.append((y + dy, x + dx))
        if mat[y + dy][x + dx] == "P":
            res += 1

if res > 0:
    print(res)
else:
    print("TT")
