import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
INF = 10**9
dist = [INF] * 100001

dist[N] = 0
q = deque([N])
while q:
    cur = q.popleft()
    if cur == K:
        print(dist[cur])
        break
    for to in [cur - 1, cur + 1, cur * 2]:
        if 0 <= to <= 100000 and dist[cur] + 1 < dist[to]:
            dist[to] = dist[cur] + (0 if to == cur * 2 else 1)
            q.append(to)
