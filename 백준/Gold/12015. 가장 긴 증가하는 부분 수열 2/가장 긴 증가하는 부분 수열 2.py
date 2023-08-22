import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
stk = [0] * N
res = -1  # 스택의 마지막 원소를 가리킴


def binary_search(start, end, target):  # 이분 탐색의 시간복잡도는 O(log N)
    global stk

    if start >= end:
        return start

    mid = (start + end) // 2

    if target > stk[mid]:
        return binary_search(mid + 1, end, target)
    return binary_search(start, mid, target)


for num in arr:
    if res == -1 or num > stk[res]:  # 스택이 비었거나 현재 숫자가 스택의 마지막 원소보다 크다면 삽입
        res += 1
        stk[res] = num
    else:
        idx = binary_search(0, res, num)  # 그렇지 않다면 대체할 수 있는 중간의 숫자를 찾아 들어감
        stk[idx] = num

if res >= 0:
    print(res + 1)
else:
    print(0)
