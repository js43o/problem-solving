import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split(" ")))
stk = []
last = -1


def binary_search(start, end, target):
    if start >= end:
        return start

    mid = (start + end) // 2
    if target <= stk[mid]:
        return binary_search(start, mid, target)
    if target > stk[mid]:
        return binary_search(mid + 1, end, target)


for elem in arr:
    if last == -1 or elem > stk[last]:
        stk.append(elem)
        last += 1
        continue

    idx = binary_search(0, last, elem)
    stk[idx] = elem

print(last + 1)
