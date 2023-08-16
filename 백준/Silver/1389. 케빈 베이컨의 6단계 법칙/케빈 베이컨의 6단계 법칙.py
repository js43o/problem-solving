import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)


def bfs(init):
    q = deque([init])
    kevin = [0] * (N + 1)
    sum = 0

    while q:
        v = q.popleft()
        for i in arr[v]:
            if i != init and kevin[i] == 0:  # 방문하지 않았다면
                q.append(i)
                kevin[i] = kevin[v] + 1
                sum += kevin[i]
    return sum


min = -1
res = 0
for i in range(1, N + 1):
    k = bfs(i)
    if min == -1 or min > k:
        min = k
        res = i

print(res)
