import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    a = 1
    b = 1
    for i in range(N):
        a *= M - i
        b *= i + 1

    print(a // b)
