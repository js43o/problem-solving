import sys

input = sys.stdin.readline

N = int(input())
isStack = list(map(int, input().split()))
queuestack = list(map(int, input().split()))
M = int(input())
result = []

for i in range(len(queuestack) - 1, -1, -1):
    if not isStack[i]:
        result.append(queuestack[i])

C = list(map(int, input().split()))
result.extend(C)

print(*result[:M])
