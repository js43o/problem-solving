import sys

N = int(input())
matrix = []
result = []

for _ in range(N):
    matrix.append(list(sys.stdin.readline().rstrip()))


def quad(n, top, left):
    if n == 1:
        result.append(matrix[top][left])
        return

    first = matrix[top][left]

    for i in range(top, top + n):
        for j in range(left, left + n):
            if matrix[i][j] != first:
                result.append("(")
                quad(n // 2, top, left)
                quad(n // 2, top, left + n // 2)
                quad(n // 2, top + n // 2, left)
                quad(n // 2, top + n // 2, left + n // 2)
                result.append(")")
                return

    result.append(first)


quad(N, 0, 0)
print("".join(result))
