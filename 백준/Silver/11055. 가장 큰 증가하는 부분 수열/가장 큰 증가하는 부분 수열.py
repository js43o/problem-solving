import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [0] * N
dp[0] = arr[0]

for i in range(1, N):
    maxVal = 0
    for j in range(i):
        if arr[j] < arr[i] and dp[j] > maxVal:
            maxVal = dp[j]
    dp[i] = maxVal + arr[i]

print(max(dp))
