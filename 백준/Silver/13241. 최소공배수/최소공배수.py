import sys

input = sys.stdin.readline


def gcd(a, b):
    if b > a:
        a, b = b, a

    while b > 0:
        a, b = b, a % b

    return a


A, B = map(int, input().split())
print((A * B) // gcd(A, B))
