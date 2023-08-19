import sys

input = sys.stdin.readline
T = int(input().rstrip())

for _ in range(T):
    p = input().rstrip()
    n = int(input().rstrip())
    a = input().rstrip()
    arr = list(map(int, a[1:-1].split(","))) if len(a) > 2 else []
    flag = True
    isError = False
    start, end = 0, n
    for oper in p:
        if oper == "R":
            flag = not flag
        else:
            if start >= end:
                isError = True
                break
            if flag:
                start += 1
            else:
                end -= 1

    if isError:
        print("error")
    elif flag:
        print("[", end="")
        for i in range(start, end):
            print(arr[i], end="")
            print(",", end="") if i < end - 1 else ""
        print("]")
    else:
        print("[", end="")
        for i in range(end - 1, start - 1, -1):
            print(arr[i], end="")
            print(",", end="") if i > start else ""
        print("]")
