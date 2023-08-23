import sys

input = sys.stdin.readline

N, S = map(int, input().split())
arr = [0] + list(map(int, input().split()))
acc = [0] * (N + 1)  # 0번째 요소는 0으로, 1부터 N까지 누적시키기
res = N + 1

for i in range(1, N + 1):
    acc[i] = acc[i - 1] + arr[i]

start = 0
end = 1
while end <= N:
    if acc[end] - acc[start] >= S:
        res = min(res, end - start)
        start += 1
    else:
        end += 1

if res < N + 1:
    print(res)
else:
    print(0)
