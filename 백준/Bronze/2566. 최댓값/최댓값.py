import sys

input = sys.stdin.readline

mat = []
maxVal = 0
maxPos = None

for i in range(9):
    arr = list(map(int, input().split()))
    for j in range(len(arr)):
        if arr[j] >= maxVal:
            maxVal = arr[j]
            maxPos = (i + 1, j + 1)

print(maxVal)
print(maxPos[0], maxPos[1])
