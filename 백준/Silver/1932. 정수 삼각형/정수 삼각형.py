import sys

input = sys.stdin.readline

n = int(input())
prev = []
res = 0
for l in range(n):
    arr = list(map(int, input().split()))
    if l == 0:
        prev = arr
        continue

    arr[0] += prev[0]
    for i in range(1, l + 1):
        if i == l:
            arr[i] += prev[l - 1]
        else:
            arr[i] += max(prev[i], prev[i - 1])
    prev = arr

print(max(prev))
