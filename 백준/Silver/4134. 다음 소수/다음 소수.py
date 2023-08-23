import sys

input = sys.stdin.readline


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            return False
    return True


T = int(input())
for _ in range(T):
    n = int(input())
    while True:
        if isPrime(n):
            print(n)
            break
        n += 1
