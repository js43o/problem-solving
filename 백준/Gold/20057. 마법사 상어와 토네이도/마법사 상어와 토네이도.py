import sys

input = sys.stdin.readline


def moveTornado():
    global cur, level, direction

    curY, curX = cur
    startY, startX = start[0] + 0.5, start[1] - 0.5

    if curY == curX + 1 and curX > startX and curY > startY:  # level-up
        curX += 1
        level += 1
    else:
        if curX < startX - level and curY < startY + level:  # down
            curY += 1
            direction = "DOWN"
        elif curY > startY + level and curX < startX + level:  # right
            curX += 1
            direction = "RIGHT"
        elif curX > startX + level and curY > startY - level:  # up
            curY -= 1
            direction = "UP"
        elif curY <= startY - level and curX > startX - level:  # left
            curX -= 1
            direction = "LEFT"

    cur = (curY, curX)
    return direction


def moveSand():
    global cur, start, level, direction

    curY, curX = cur
    startY, startX = start[0] + 0.5, start[1] - 0.5
    curSand = mat[curY][curX]
    addSand = [
        int(curSand * 0.10),
        int(curSand * 0.07),
        int(curSand * 0.02),
        int(curSand * 0.01),
        int(curSand * 0.05),
    ]
    addSand.append(curSand - sum((2 * addSand)[:-1]))  # last sand
    movePos = None
    mat[curY][curX] = 0

    if direction == "LEFT":  # left
        movePos = [
            (-1, -1, 0),
            (1, -1, 0),
            (-1, 0, 1),
            (1, 0, 1),
            (-2, 0, 2),
            (2, 0, 2),
            (-1, 1, 3),
            (1, 1, 3),
            (0, -2, 4),
            (0, -1, 5),
        ]
    elif direction == "DOWN":  # down
        movePos = [
            (1, -1, 0),
            (1, 1, 0),
            (0, -1, 1),
            (0, 1, 1),
            (0, -2, 2),
            (0, 2, 2),
            (-1, -1, 3),
            (-1, 1, 3),
            (2, 0, 4),
            (1, 0, 5),
        ]
    elif direction == "RIGHT":  # right
        movePos = [
            (-1, 1, 0),
            (1, 1, 0),
            (-1, 0, 1),
            (1, 0, 1),
            (-2, 0, 2),
            (2, 0, 2),
            (-1, -1, 3),
            (1, -1, 3),
            (0, 2, 4),
            (0, 1, 5),
        ]
    elif direction == "UP":  # up
        movePos = [
            (-1, -1, 0),
            (-1, 1, 0),
            (0, -1, 1),
            (0, 1, 1),
            (0, -2, 2),
            (0, 2, 2),
            (1, -1, 3),
            (1, 1, 3),
            (-2, 0, 4),
            (-1, 0, 5),
        ]

    for dy, dx, idx in movePos:
        mat[curY + dy][curX + dx] += addSand[idx]


N = int(input())
mat = [[0] * (N + 4) for _ in range(2)]
start = (2 + N // 2, 2 + N // 2)
cur = start
level = 0
res = 0
direction = "LEFT"

for _ in range(N):
    arr = list(map(int, input().split(" ")))
    mat.append([0, 0] + arr + [0, 0])
mat.append([0] * (N + 4))
mat.append([0] * (N + 4))

moveTornado()
while cur[0] >= 2 and cur[1] >= 2:
    moveSand()
    moveTornado()

tmp = 0
for i in range(N + 4):
    tmp += sum(mat[i])
    if i <= 1 or i >= N + 2:
        res += sum(mat[i])
    else:
        res += sum(mat[i][:2]) + sum(mat[i][-2:])

print(res)
