import sys

input = sys.stdin.readline


def drawHorizontal(mat, s, drawType):
    if "UPPER" in drawType:
        for i in range(1, s + 1):
            mat[0][i] = "-"
    if "MIDDLE" in drawType:
        for i in range(1, s + 1):
            mat[s + 1][i] = "-"
    if "LOWER" in drawType:
        for i in range(1, s + 1):
            mat[2 * s + 2][i] = "-"
    return mat


def drawVertical(mat, s, drawType):
    if "TOP_LEFT" in drawType:
        for i in range(1, s + 1):
            mat[i][0] = "|"
    if "TOP_RIGHT" in drawType:
        for i in range(1, s + 1):
            mat[i][s + 1] = "|"
    if "BOTTOM_LEFT" in drawType:
        for i in range(s + 2, 2 * s + 2):
            mat[i][0] = "|"
    if "BOTTOM_RIGHT" in drawType:
        for i in range(s + 2, 2 * s + 2):
            mat[i][s + 1] = "|"
    return mat


def drawNum(s, num):
    num = int(num)
    mat = [[" "] * (s + 2) for _ in range(2 * s + 3)]

    if num == 0:
        mat = drawHorizontal(mat, s, ["UPPER", "LOWER"])
        mat = drawVertical(
            mat, s, ["TOP_LEFT", "TOP_RIGHT", "BOTTOM_LEFT", "BOTTOM_RIGHT"]
        )
    elif num == 1:
        mat = drawVertical(mat, s, ["TOP_RIGHT", "BOTTOM_RIGHT"])
    elif num == 2:
        mat = drawHorizontal(mat, s, ["UPPER", "MIDDLE", "LOWER"])
        mat = drawVertical(mat, s, ["TOP_RIGHT", "BOTTOM_LEFT"])
    elif num == 3:
        mat = drawHorizontal(mat, s, ["UPPER", "MIDDLE", "LOWER"])
        mat = drawVertical(mat, s, ["TOP_RIGHT", "BOTTOM_RIGHT"])
    elif num == 4:
        mat = drawHorizontal(mat, s, ["MIDDLE"])
        mat = drawVertical(mat, s, ["TOP_LEFT", "TOP_RIGHT", "BOTTOM_RIGHT"])
    elif num == 5:
        mat = drawHorizontal(mat, s, ["UPPER", "MIDDLE", "LOWER"])
        mat = drawVertical(mat, s, ["TOP_LEFT", "BOTTOM_RIGHT"])
    elif num == 6:
        mat = drawHorizontal(mat, s, ["UPPER", "MIDDLE", "LOWER"])
        mat = drawVertical(mat, s, ["TOP_LEFT", "BOTTOM_LEFT", "BOTTOM_RIGHT"])
    elif num == 7:
        mat = drawHorizontal(mat, s, ["UPPER"])
        mat = drawVertical(mat, s, ["TOP_RIGHT", "BOTTOM_RIGHT"])
    elif num == 8:
        mat = drawHorizontal(mat, s, ["UPPER", "MIDDLE", "LOWER"])
        mat = drawVertical(
            mat, s, ["TOP_LEFT", "TOP_RIGHT", "BOTTOM_LEFT", "BOTTOM_RIGHT"]
        )
    elif num == 9:
        mat = drawHorizontal(mat, s, ["UPPER", "MIDDLE", "LOWER"])
        mat = drawVertical(mat, s, ["TOP_LEFT", "TOP_RIGHT", "BOTTOM_RIGHT"])

    return mat


s, n = input().split()
s = int(s)

res = [[" "] * ((s + 3) * len(n) + 1) for _ in range(2 * s + 3)]
idx = 0

for num in n:
    mat = drawNum(s, num)
    for y in range(0, 2 * s + 3):
        for x in range(0, s + 2):
            res[y][idx + x] = mat[y][x]
    idx += s + 3

for y in range(2 * s + 3):
    for x in range((s + 3) * len(n) + 1):
        print(res[y][x], end="")
    if y != 2 * s + 2:
        print()
