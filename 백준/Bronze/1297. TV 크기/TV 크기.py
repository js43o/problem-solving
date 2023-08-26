import sys

input = sys.stdin.readline

D, H, W = map(int, input().split())

X = D / ((W**2 + H**2) ** (1 / 2))

print(int(X * H), int(X * W))
