import sys

sys.setrecursionlimit(10 ** 9)

N = int(input())
matrix = []

for _ in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

dict = [0, 0, 0]  # dict[0] == "-1", dict[1] = "0", dict[2] = "1"


def divide(n, top, left):
    if n == 1:
        dict[matrix[top][left] + 1] += 1
        return

    isSame = True
    first = matrix[top][left]

    for i in range(top, top + n):
        for j in range(left, left + n):
            if matrix[i][j] != first:
                isSame = False
                break
        if not isSame:
            break

    if isSame:
        dict[first + 1] += 1
        return

    for i in range(top, top + n, n // 3):
        for j in range(left, left + n, n // 3):
            divide(n // 3, i, j)


divide(N, 0, 0)

for i in dict:
    print(i)
