import sys
from collections import deque

N = int(input())
matrix = []
house = deque()
result = []

for _ in range(N):
    matrix.append(list(sys.stdin.readline().rstrip()))

for y in range(N):
    for x in range(N):
        if matrix[y][x] == "1":
            house.append((y, x))


def bfs(init_y, init_x):
    q = deque([(init_y, init_x)])
    matrix[init_y][init_x] = "0"
    count = 1

    while q:
        y, x = q.popleft()
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= y + dy < N and 0 <= x + dx < N:
                if matrix[y + dy][x + dx] == "1":
                    matrix[y + dy][x + dx] = "0"
                    q.append((y + dy, x + dx))
                    count += 1

    result.append(count)


while house:
    y, x = house.popleft()
    if matrix[y][x] == "1":
        bfs(y, x)

result.sort()
print(len(result))
for a in result:
    print(a)
