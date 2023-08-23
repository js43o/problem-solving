import sys

input = sys.stdin.readline

N = int(input())
signal = input().rstrip()
cutNum = N // 5
mat = []
res = ""
x = 0


def readNum(mat, x):
    if x + 2 >= cutNum:
        if mat[0][x] == mat[1][x] == mat[2][x] == mat[3][x] == mat[4][x] == "#":
            return 1
        else:
            return -1

    if mat[0][x] == mat[1][x] == mat[2][x] == mat[3][x] == mat[4][x] == "#":  # 세로 긴 변
        if (
            mat[0][x + 2]
            == mat[1][x + 2]
            == mat[2][x + 2]
            == mat[3][x + 2]
            == mat[4][x + 2]
            == "#"
        ):  # 우측 긴 변
            if mat[0][x + 1] == mat[2][x + 1] == mat[4][x + 1] == "#":  # 가로 3개
                return 8
            elif mat[0][x + 1] == mat[4][x + 1] == "#":  # 가로 2개
                return 0
        elif (
            mat[0][x + 2] == mat[2][x + 2] == mat[3][x + 2] == mat[4][x + 2] == "#"
        ):  # 1번째 자리만 빠지고
            if mat[0][x + 1] == mat[2][x + 1] == mat[4][x + 1] == "#":  # 가로 3개
                return 6
        return 1
    elif mat[0][x] == mat[0][x + 1] == mat[0][x + 2] == "#":  # 가로 맨 위
        if mat[2][x] == mat[2][x + 1] == mat[2][x + 2] == "#":  # 가로 가운데
            if mat[4][x] == mat[4][x + 1] == mat[4][x + 2] == "#":  # 가로 맨 밑
                if mat[1][x + 2] == mat[3][x + 2] == "#":
                    if mat[1][x] == "#":
                        return 9
                    return 3
                elif mat[1][x + 2] == mat[3][x] == "#":
                    return 2
                elif mat[1][x] == mat[3][x + 2] == "#":
                    return 5
    elif mat[0][x] == mat[1][x] == mat[2][x] == "#":
        return 4
    return 7


for i in range(5):
    mat.append(signal[i * cutNum : i * cutNum + cutNum])

while x < cutNum:
    if mat[0][x] != "#":
        x += 1
        continue
    num = readNum(mat, x)
    if num == -1:
        break
    res += str(num)
    x += 2 if num == 1 else 4

print(res)
