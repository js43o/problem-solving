import sys

input = sys.stdin.readline
bingo = []
pos = {}
res = 0


def checkBingo():
    res = 0
    for i in range(5):
        if bingo[0][i] == bingo[1][i] == bingo[2][i] == bingo[3][i] == bingo[4][i] == 0:
            res += 1
        if bingo[i][0] == bingo[i][1] == bingo[i][2] == bingo[i][3] == bingo[i][4] == 0:
            res += 1
    if bingo[0][0] == bingo[1][1] == bingo[2][2] == bingo[3][3] == bingo[4][4] == 0:
        res += 1
    if bingo[0][4] == bingo[1][3] == bingo[2][2] == bingo[3][1] == bingo[4][0] == 0:
        res += 1

    return res


for i in range(5):
    arr = input().split()
    bingo.append(arr)
    for j in range(len(arr)):
        pos[arr[j]] = (i, j)

for i in range(5):
    arr = input().split()
    for j in range(len(arr)):
        y, x = pos[arr[j]]
        bingo[y][x] = 0
        if res == 0 and checkBingo() >= 3:
            res = i * 5 + j + 1

print(res)
