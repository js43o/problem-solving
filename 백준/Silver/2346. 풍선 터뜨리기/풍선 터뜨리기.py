import sys
from collections import deque

input = sys.stdin.readline


N = int(input())
balloons = list(map(int, input().split()))
target = 0
result = []


# direction == 1(오른쪽) or -1(왼쪽)
def moveTarget(offset, direction):
    global target
    while offset > 0:
        if balloons[(target + direction) % N] != None:
            offset -= 1
        target = (target + direction) % N


for _ in range(N - 1):
    offset = balloons[target]
    balloons[target] = None
    result.append(target + 1)
    moveTarget(abs(offset), 1 if offset > 0 else -1)

print(*result, target + 1)
