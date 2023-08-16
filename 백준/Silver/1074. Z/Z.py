import sys

sys.setrecursionlimit(10 ** 9)

N, R, C = map(int, sys.stdin.readline().split())


def find_number(n, left_top, r, c):
    if n == 0:
        print(left_top)
        return

    if r < 2 ** (n - 1):
        if c < 2 ** (n - 1):
            find_number(n - 1, left_top, r, c)
        else:
            find_number(n - 1, left_top + 2 ** (2 * (n - 1)) * 1, r, c - 2 ** (n - 1))
    else:
        if c < 2 ** (n - 1):
            find_number(n - 1, left_top + 2 ** (2 * (n - 1)) * 2, r - 2 ** (n - 1), c)
        else:
            find_number(
                n - 1,
                left_top + 2 ** (2 * (n - 1)) * 3,
                r - 2 ** (n - 1),
                c - 2 ** (n - 1),
            )


find_number(N, 0, R, C)
