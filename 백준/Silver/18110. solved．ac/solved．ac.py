import sys

input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    s = int(input())
    lst.append(s)
lst.sort()


def myRound(n):
    if n - int(n) >= 0.5:
        return int(n) + 1
    else:
        return int(n)


if n == 0:
    print(0)
else:
    cutNum = myRound(n * 0.15)
    res = myRound(sum(lst[cutNum : n - cutNum]) / (n - cutNum * 2))
    print(res)
