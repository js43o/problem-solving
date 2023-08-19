import sys, functools

T = int(input())

for _ in range(T):
    N = int(input())
    dict = {}
    for _ in range(N):
        name, key = sys.stdin.readline().split()
        if key not in dict:
            dict[key] = 1
        dict[key] += 1

    result = functools.reduce(lambda acc, cur: acc * int(dict[cur]), list(dict), 1)
    print(result - 1)
