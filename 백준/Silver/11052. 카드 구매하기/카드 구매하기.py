import sys

input = sys.stdin.readline

N = int(input())
price = [0] + list(map(int, input().split()))
dp = [0] * (N + 1)  # 총 카드를 n장 구매했을 때의 최대 비용
res = 0

dp[1] = price[1]  # 카드 1장 구매 비용 = 카드가 1개 들어있는 카드팩 구매

for i in range(2, N + 1):  # 2 <= i <= N
    for j in range(i):  # 0 <= j <= i-1
        dp[i] = max(dp[i], dp[j] + price[i - j])


print(dp[N])
