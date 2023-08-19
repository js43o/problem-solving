import sys

input = sys.stdin.readline

while True:
    N = int(input())
    if N == -1:
        break

    divisors = []
    for q in range(1, N):
        if N % q == 0:
            divisors.append(q)

    if sum(divisors) == N:
        print("%d = %s" % (N, " + ".join(map(str, divisors))))
    else:
        print("%s is NOT perfect." % N)
