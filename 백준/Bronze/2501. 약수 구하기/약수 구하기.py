import sys

input = sys.stdin.readline

N, K = map(int, input().split())
count = 0
result = 0

for q in range(1, N + 1):
    if N % q == 0:
        count += 1
    if count == K:
        result = q
        break

print(result)
