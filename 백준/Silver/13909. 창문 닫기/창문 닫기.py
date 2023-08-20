import sys

input = sys.stdin.readline

N = int(input())
result = 0

for i in range(1, int(N ** (0.5)) + 1):
    if N % 1 == 0:
        result += 1

print(result)
