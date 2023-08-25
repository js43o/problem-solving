import sys

N, K = map(int, sys.stdin.readline().split())
arr = []

for _ in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))

arr.sort(reverse=True)

count = 0
i = 0

while K > 0:
    if arr[i] > K:
        i += 1
        continue
    count += K // arr[i]
    K %= arr[i]

print(count)
