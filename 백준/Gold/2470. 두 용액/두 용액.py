import sys

input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))
minValue = 10**10
result = None


def binary_search(start, end, value):
    global minValue, result

    if start >= end:
        return

    mid = (start + end) // 2
    newValue = value + arr[mid]

    if abs(newValue) < minValue and value != arr[mid]:
        minValue = abs(newValue)
        result = (value, arr[mid])

    if newValue > 0:
        binary_search(start, mid, value)
    elif newValue < 0:
        binary_search(mid + 1, end, value)
    else:
        return


arr.sort()
for value in arr:
    binary_search(0, N, value)

print(*sorted(result))
