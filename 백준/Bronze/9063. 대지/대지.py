import sys

input = sys.stdin.readline

N = int(input())
min_y, min_x = 10001, 10001
max_y, max_x = -10001, -10001
for _ in range(N):
    y, x = map(int, input().split())
    min_y = min(min_y, y)
    min_x = min(min_x, x)
    max_y = max(max_y, y)
    max_x = max(max_x, x)

print((max_y - min_y) * (max_x - min_x))
