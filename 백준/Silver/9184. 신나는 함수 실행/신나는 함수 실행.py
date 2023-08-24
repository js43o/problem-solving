import sys

dic = {}


def trans(a, b, c):
    return "%d_%d_%d" % (a, b, c)


def w(a, b, c):
    if trans(a, b, c) in dic:
        return dic[trans(a, b, c)]
    else:
        result = 0

        if a <= 0 or b <= 0 or c <= 0:
            result = 1
        elif a > 20 or b > 20 or c > 20:
            result = w(20, 20, 20)
        elif a < b and b < c:
            result = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        else:
            result = (
                w(a - 1, b, c)
                + w(a - 1, b - 1, c)
                + w(a - 1, b, c - 1)
                - w(a - 1, b - 1, c - 1)
            )

        dic[trans(a, b, c)] = result
        return result


while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == b == c == -1:
        break
    print("w(%d, %d, %d) = %d" % (a, b, c, w(a, b, c)))
