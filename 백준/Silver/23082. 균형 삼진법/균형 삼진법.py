from re import I
import sys

input = sys.stdin.readline


def three(n):
    result = []
    flag = False

    if n < 0:
        n = -n
        flag = True
    elif n == 0:
        return [0]

    while n > 0:
        if n % 3 < 2:
            result.append(str(n % 3))
            n = n // 3
        else:
            result.append("T")
            n = n // 3 + 1

    if flag:
        for i in range(len(result)):
            if result[i] == "T":
                result[i] = "1"
            elif result[i] == "1":
                result[i] = "T"

    return reversed(result)


n = int(input())
print(*three(n), sep="")
