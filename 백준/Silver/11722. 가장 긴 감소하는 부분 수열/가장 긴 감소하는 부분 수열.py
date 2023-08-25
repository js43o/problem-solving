n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n

for i in range(n):
    m = 0
    for j in range(i):
        if arr[i] < arr[j]:
            m = max(m, dp[j])
    dp[i] = m + 1

print(max(dp))
