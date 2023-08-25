import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
acc = arr.copy()
for i in range(1, len(arr)):
    acc[i] = acc[i] + acc[i - 1]


for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    if i > 1:
        print(acc[j - 1] - acc[i - 2])
    else:
        print(acc[j - 1])
