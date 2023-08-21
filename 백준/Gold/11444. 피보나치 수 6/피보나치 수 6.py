import sys

input = sys.stdin.readline

N = int(input())
D = 1000000007


def multi(a, b):
    temp = [[0] * len(b[0]) for _ in range(2)]
    for i in range(2):
        for j in range(len(b[0])):
            sum = 0
            for k in range(2):
                sum += a[i][k] * b[k][j]
            temp[i][j] = sum % D
    return temp


def power(mat, i):
    if i == 1:
        return mat
    elif i % 2 == 0:
        return power(multi(mat, mat), i // 2)
    else:
        return multi(power(mat, i - 1), mat)


def fibonacci(n):
    if n < 3:
        return 1
    result = [[1, 1], [1, 0]]
    start = [[1], [1]]
    return multi(power(result, n - 2), start)[0][0]


print(fibonacci(N))
