import sys

input = sys.stdin.readline


def isInside(x, y, circleX, circleY, r):
    dist = (((y - circleY) ** 2) + ((x - circleX) ** 2)) ** (1 / 2)
    return dist <= r


T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    result = 0
    for __ in range(n):
        cx, cy, r = map(int, input().split())
        if (isInside(x1, y1, cx, cy, r) and not isInside(x2, y2, cx, cy, r)) or (
            not isInside(x1, y1, cx, cy, r) and isInside(x2, y2, cx, cy, r)
        ):
            result += 1

    print(result)
