import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split(" "))
mat = []
dist = [[0] * m for _ in range(n)]
start = None

for y in range(n):
    arr = list(map(int, input().split(" ")))
    mat.append(arr)
    if 2 in arr:
        start = (y, arr.index(2))

q = deque([start])
while q:
    y, x = q.popleft()
    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if 0 <= y + dy < n and 0 <= x + dx < m and mat[y + dy][x + dx] == 1:
            if dist[y + dy][x + dx] == 0:
                dist[y + dy][x + dx] = dist[y][x] + 1
                q.append((y + dy, x + dx))

for y in range(n):
    for x in range(m):
        if dist[y][x] == 0 and mat[y][x] == 1:
            dist[y][x] = -1

for y in range(n):
    for x in range(m):
        print(dist[y][x], end=" ")
    print()
