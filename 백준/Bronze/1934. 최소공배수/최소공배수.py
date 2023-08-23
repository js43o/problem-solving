import sys

input = sys.stdin.readline

T = int(input())


def gcd(a, b):
    if a < b:
        a, b = b, a  # swap

    while b > 0:
        r = a % b
        a = b
        b = r

    return a


for _ in range(T):
    A, B = map(int, input().split())
    print(int(A * B / gcd(A, B)))
