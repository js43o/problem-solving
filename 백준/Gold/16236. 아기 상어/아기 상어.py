import sys, copy
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())
matrix = []
coord_x, coord_y = 0, 0

for _ in range(N):
    arr = list(map(int, input().split()))
    if 9 in arr:
        coord_y, coord_x = (_, arr.index(9))
        arr[coord_x] = 0
    matrix.append(arr)


def find_food(init_y, init_x, size, count):
    q = deque([(init_y, init_x)])
    eatable = []
    visited = [[0] * N for _ in range(N)]

    while q:
        y, x = q.popleft()

        for dy, dx in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            if (
                0 <= y + dy < N
                and 0 <= x + dx < N
                and visited[y + dy][x + dx] == 0
                and matrix[y + dy][x + dx] <= size
            ):
                if (
                    matrix[y + dy][x + dx] == 0 or matrix[y + dy][x + dx] == size
                ):  # 이동만 가능할 시
                    q.append((y + dy, x + dx))
                    visited[y + dy][x + dx] = visited[y][x] + 1
                elif 0 < matrix[y + dy][x + dx] < size:  # 먹이 발견 시
                    visited[y + dy][x + dx] = visited[y][x] + 1
                    eatable.append((visited[y + dy][x + dx], y + dy, x + dx))

    if len(eatable) > 0:
        eatable.sort() # count, y, x 순으로 정렬
        c, y, x = eatable[0]
        matrix[y][x] = 0
        return (count + c, y, x)
    
    return (count, -1, -1)


stomach = 2
eat = 0
count = 0

while True:
    count, coord_y, coord_x = find_food(coord_y, coord_x, stomach, count)

    if coord_y > -1 and coord_x > -1:
        eat += 1
        if eat >= stomach:
            stomach += 1
            eat = 0
    else:
        break


print(count)
