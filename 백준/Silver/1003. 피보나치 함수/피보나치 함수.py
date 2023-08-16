import sys

arr = [[1, 0], [0, 1]]

T = int(input())

for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    res = arr.copy()
    for i in range(2, n + 1):
        res.append([res[i - 2][0] + res[i - 1][0], res[i - 2][1] + res[i - 1][1]])
    print("%d %d" % (res[n][0], res[n][1]))
