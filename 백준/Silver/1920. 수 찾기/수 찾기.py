import sys, math

n = int(input())
arr1 = sorted(list(map(int, sys.stdin.readline().split())))

m = int(input())
arr2 = list(map(int, sys.stdin.readline().split()))


def binary_search(left, mid, right, k):
    if left > right:
        print(0)
        return
    if k > arr1[mid]:
        binary_search(mid + 1, math.floor((right + mid + 1) / 2), right, k)
    elif k < arr1[mid]:
        binary_search(left, math.floor((left + mid - 1) / 2), mid - 1, k)
    else:
        print(1)


for i in arr2:
    binary_search(0, math.floor((n - 1) / 2), n - 1, i)
