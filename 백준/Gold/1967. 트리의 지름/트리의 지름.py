import sys

input = sys.stdin.readline

sys.setrecursionlimit(10 ** 9)

N = int(input().rstrip())
arr = [[] for _ in range(N + 1)]


def trav(v, weight):
    for b, w in arr[v]:
        if dist[b] == -1:
            dist[b] = weight + w
            trav(b, weight + w)


for _ in range(N - 1):
    a, b, w = map(int, input().split())
    arr[a].append((b, w))
    arr[b].append((a, w))

dist = [-1] * (N + 1)
dist[1] = 0
trav(1, 0)

mid = dist.index(max(dist))
dist = [-1] * (N + 1)
dist[mid] = 0
trav(mid, 0)

print(max(dist))
