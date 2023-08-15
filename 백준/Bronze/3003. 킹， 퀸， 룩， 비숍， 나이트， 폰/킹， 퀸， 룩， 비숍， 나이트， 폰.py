import sys

input = sys.stdin.readline

ori = [1, 1, 2, 2, 2, 8]
arr = list(map(int, input().split(" ")))

for i in range(len(ori)):
    print(ori[i] - arr[i], end=" ")
