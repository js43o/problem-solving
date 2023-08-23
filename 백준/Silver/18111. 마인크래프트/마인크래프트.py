import sys, math

N, M, B = map(int, input().split())
arr = []
total = B

for _ in range(N):
    i = list(map(int, sys.stdin.readline().split()))
    arr += i
    total += sum(i)

max_height = math.floor(total / (N * M))
result_time = 999999999999
result_height = 0

# 최종적으로 inven >= 0이 보장됨.
for avg in range(max_height + 1):
    time = 0
    for i in arr:
        if i > avg:
            time += (i - avg) * 2
        elif i < avg:
            time += avg - i
        if time > result_time:
            break
    if time < result_time:
        result_time = time
        result_height = avg
    elif time == result_time and avg > result_height:
        result_height = avg

print("%d %d" % (result_time, result_height))
