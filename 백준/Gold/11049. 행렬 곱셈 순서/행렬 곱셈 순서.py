import sys

input = sys.stdin.readline
MAX = 2**32

N = int(input())
mat = []
dp = [[0] * N for _ in range(N)]

for i in range(N):
    dp[i][i] = 0
    r, c = map(int, input().split())
    mat.append((r, c))

for offset in range(1, N):
    for start in range(N - offset):
        end = start + offset  # [start, end] 범위 내의 행렬들에 대한 곱셈의 최솟값 구하기

        if offset == 1:  # 두 행렬 간 곱셈일 때
            dp[start][end] = mat[start][0] * mat[start][1] * mat[end][1]
            continue

        dp[start][end] = MAX
        for mid in range(start, end):  # 중간 지점을 분할함. ABCD => (A)BCD, (AB)CD, (ABC)D
            dp[start][end] = min(
                dp[start][end],
                dp[start][mid]
                + dp[mid + 1][end]
                + mat[start][0] * mat[mid][1] * mat[end][1],
            )  # 각각의 곱셈의 최솟값에 두 행렬곱의 연산 횟수를 더함

print(dp[0][N - 1])
