from collections import deque

MAX = 10 ** 5
dist = [0] * (MAX + 1)
N, K = map(int, input().split())


def bfs():
    queue = deque([N])
    while queue:
        v = queue.popleft()

        if v == K:
            print(dist[v])
            break

        for dv in [v - 1, v + 1, v * 2]:
            if 0 <= dv <= MAX and not dist[dv]:
                dist[dv] = dist[v] + 1
                queue.append(dv)


bfs()
