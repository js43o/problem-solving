import sys

input = sys.stdin.readline
matrix = []
result = [0, -1, -1]

n = int(input().rstrip())
for _ in range(n):
    matrix.append(list(input().rstrip()))


def go(i, j):
    global result
    count = 0
    for dy, dx in [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
        (-1, -1),
        (1, 1),
        (-1, 1),
        (1, -1),
    ]:
        c = 0
        y, x = i + dy, j + dx
        while 0 <= y < n and 0 <= x < n:
            if matrix[y][x] == "W":
                c += 1
                y += dy
                x += dx
            elif matrix[y][x] == "B":
                count += c
                break
            else:
                break

    if count > result[0]:
        result[0], result[1], result[2] = count, i, j
    elif count == result[0]:
        if y < result[1] or (y == result[1] and x < result[2]):
            result[1], result[2] = i, j


for i in range(n):
    for j in range(n):
        if matrix[i][j] == ".":
            go(i, j)

if result[0] == 0:
    print("PASS")
else:
    print(result[2], result[1])
    print(result[0])
