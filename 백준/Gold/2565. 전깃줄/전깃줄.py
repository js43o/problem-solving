import sys

input = sys.stdin.readline

N = int(input())
arr = []
dp = [1] * N

for _ in range(N):
    A, B = map(int, input().split())
    arr.append([A, B])

arr.sort()

for i in range(1, N):
    for j in range(i):
        if arr[j][1] < arr[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)


print(N - max(dp))
