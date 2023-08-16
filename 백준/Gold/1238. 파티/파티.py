import sys, heapq

input = sys.stdin.readline
MAX = int(1e9)

N, M, X = map(int, input().split())
arr = [[] for _ in range((N + 1))]

for _ in range(M):
    a, b, cost = map(int, input().split())
    arr[a].append((b, cost))


def dijkstra(s):
    q = []
    dist = [MAX] * (N + 1)

    dist[s] = 0
    heapq.heappush(q, (dist[s], s))

    while q:
        cost, v = heapq.heappop(q)

        if dist[v] < cost:
            continue

        for to, weight in arr[v]:
            if cost + weight < dist[to]:
                dist[to] = cost + weight
                heapq.heappush(q, (dist[to], to))

    return dist


result = 0
for i in range(1, N + 1):
    go = dijkstra(i)
    back = dijkstra(X)
    result = max(result, go[X] + back[i])

print(result)
