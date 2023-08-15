import sys

input = sys.stdin.readline

cost = 0
X = int(input())
N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    cost += a * b

print("Yes" if cost == X else "No")
