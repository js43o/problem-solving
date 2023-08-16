import sys

sys.setrecursionlimit(10 ** 9)

T = int(input())

for _ in range(T):
    M, N, T = map(int, sys.stdin.readline().split())
    garden = [[False] * M for _ in range(N)]
    coords = []
    for _ in range(T):
        column, row = map(int, sys.stdin.readline().split())
        coords.append([column, row])
        garden[row][column] = True

    def tour(x, y):
        global garden
        global coords

        coords.remove([x, y])

        # UP
        if len(coords) > 0 and y - 1 >= 0 and [x, y - 1] in coords:
            tour(x, y - 1)
        # DOWN
        if len(coords) > 0 and y + 1 < N and [x, y + 1] in coords:
            tour(x, y + 1)
        # LEFT
        if len(coords) > 0 and x - 1 >= 0 and [x - 1, y] in coords:
            tour(x - 1, y)
        # RIGHT
        if len(coords) > 0 and x + 1 < M and [x + 1, y] in coords:
            tour(x + 1, y)

    count = 0
    while len(coords) > 0:
        x, y = list(coords).pop()
        count += 1
        tour(x, y)

    print(count)
