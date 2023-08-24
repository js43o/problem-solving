import sys

input = sys.stdin.readline

R, C = map(int, input().split())
beforeMat = [["."] * (C + 2)]
afterMat = [["."] * (C + 2) for _ in range(R + 2)]
leftmost = C
rightmost = 1
topmost = C
lowest = 1
for _ in range(R):
    arr = list(input().rstrip())
    beforeMat.append(["."] + arr + ["."])
beforeMat.append(["."] * (C + 2))

for y in range(1, R + 1):
    for x in range(1, C + 1):
        if beforeMat[y][x] == ".":
            continue
        adjacent = 0
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if (
                0 <= y + dy <= R + 1
                and 0 <= x + dx <= C + 1
                and beforeMat[y + dy][x + dx] == "."
            ):
                adjacent += 1
        if adjacent <= 2:
            afterMat[y][x] = "X"
            leftmost = min(leftmost, x)
            rightmost = max(rightmost, x)
            topmost = min(topmost, y)
            lowest = max(lowest, y)


for i in range(topmost, lowest + 1):
    for j in range(leftmost, rightmost + 1):
        print(afterMat[i][j], end="")
    print()
