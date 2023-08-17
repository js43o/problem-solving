import math

N = int(input())
K = int(input())
posK = None

mat = [[0] * (N) for _ in range(N)]
start = N // 2
mat[start][start] = 1
curY = start - 1
curX = start
curVal = 2

for level in range(1, math.ceil(N // 2) + 1):
    if curY < 0:
        break
    while curX < start + level:
        mat[curY][curX] = curVal
        curX += 1
        curVal += 1
    while curY < start + level:
        mat[curY][curX] = curVal
        curY += 1
        curVal += 1
    while curX > start - level:
        mat[curY][curX] = curVal
        curX -= 1
        curVal += 1
    while curY >= start - level:
        mat[curY][curX] = curVal
        curY -= 1
        curVal += 1

for i in range(N):
    for j in range(N):
        if mat[i][j] == K:
            posK = (i + 1, j + 1)
        print("%s " % mat[i][j], end="")
    print()
print(*posK)
