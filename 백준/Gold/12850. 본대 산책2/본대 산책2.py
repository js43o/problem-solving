import sys

sys.setrecursionlimit = 10**9

input = sys.stdin.readline

D = int(input())
R = 1000000007
mat = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0],
]
mat_len = 8


def mul_mat(mat1, mat2):
    res_mat = []
    for i in range(mat_len):
        arr = []
        for j in range(mat_len):
            res = 0
            for k in range(mat_len):
                res += (mat1[i][k] * mat2[k][j]) % R
            arr.append(res % R)
        res_mat.append(arr)
    return res_mat


def pow_mat(a, b):
    if b == 1:
        return a

    res = pow_mat(a, b // 2)

    if b % 2 == 0:
        return mul_mat(res, res)
    return mul_mat(mul_mat(res, res), a)


res = pow_mat(mat, D)
print(res[0][0])
