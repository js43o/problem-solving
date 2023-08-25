import sys

input = sys.stdin.readline


def isInside(x, y, circleX, circleY, r):
    dist = (((y - circleY) ** 2) + ((x - circleX) ** 2)) ** (1 / 2)
    return dist <= r


K = int(input())
sides = []
v_max, v_idx = 0, 0
h_max, h_idx = 0, 0
for i in range(6):
    direction, length = map(int, input().split())
    sides.append((length, direction))
    if (direction == 1 or direction == 2) and length > v_max:
        v_max = length
        v_idx = i
    if (direction == 3 or direction == 4) and length > h_max:
        h_max = length
        h_idx = i

largeSquare = v_max * h_max
smallSquare = 0

if (v_idx == 5 and h_idx == 0) or (h_idx == 5 and v_idx == 0):  # 경계값은 따로 처리
    smallSquare = sides[2][0] * sides[3][0]
else:
    idx = max(v_idx, h_idx)
    smallSquare = sides[(idx + 2) % 6][0] * sides[(idx + 3) % 6][0]

print(K * (largeSquare - smallSquare))
