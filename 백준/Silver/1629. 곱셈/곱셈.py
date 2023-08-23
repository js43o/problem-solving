import sys

sys.setrecursionlimit = 10**9

input = sys.stdin.readline

A, B, C = map(int, input().split())


def pow(a, b, c):
    if b == 0:
        return 1

    res = pow(a, b // 2, c)
    res_pow = res * res

    if b % 2 == 0:
        return res_pow % c

    return (a * res_pow) % c


print(pow(A, B, C))
