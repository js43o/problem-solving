import sys

input = sys.stdin.readline

N, M = map(int, input().split())
words = set([input().rstrip() for _ in range(N)])
checks = [input().rstrip() for _ in range(M)]
result = 0
for check in checks:
    if check in words:
        result += 1

print(result)
