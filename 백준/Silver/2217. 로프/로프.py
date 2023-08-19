import sys

input = sys.stdin.readline

N = int(input())
weights = []
for _ in range(N):
    weights.append(int(input()))
weights.sort(reverse=True)
result = 0

for i in range(len(weights)):
    result = max(result, weights[i] * (i + 1))

print(result)
