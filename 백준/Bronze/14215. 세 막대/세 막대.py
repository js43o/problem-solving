import sys

input = sys.stdin.readline


a, b, c = map(int, input().split())
arr = sorted([a, b, c])
print(arr[0] + arr[1] + min(arr[0] + arr[1] - 1, arr[2]))
