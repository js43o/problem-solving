import sys

input = sys.stdin.readline

operations = list(map(int, input().split()))
N = len(operations)
INF = 10**9
# dp[현재 명령][왼쪽 발][오른쪽 발] = 지금까지 사용된 최소 힘
dp = [[[INF for r in range(5)] for l in range(5)] for p in range(len(operations))]
dp[0][0][0] = 0
result = INF


def getPower(a, b):  # 두 발판 간 이동 시 필요한 힘 반환
    if a == b:
        return 1
    if a == 0 or b == 0:
        return 2
    if abs(a - b) == 2:
        return 4
    return 3


for i in range(N - 1):
    oper = operations[i]
    for left in range(5):
        for right in range(5):
            # 왼발 이동
            dp[i + 1][oper][right] = min(
                dp[i + 1][oper][right], dp[i][left][right] + getPower(left, oper)
            )
            # 오른발 이동
            dp[i + 1][left][oper] = min(
                dp[i + 1][left][oper], dp[i][left][right] + getPower(right, oper)
            )

for left in range(5):
    for right in range(5):
        result = min(
            result,
            dp[N - 1][operations[N - 2]][right],
            dp[N - 1][left][operations[N - 2]],
        )

print(result)
