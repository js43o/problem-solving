import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

V = int(input().rstrip())
tree = [[] for _ in range(V + 1)]

for _ in range(V):
    lst = list(map(int, input().split()))
    pairs = lst[1:-1]
    for i in range(1, len(pairs), 2):
        tree[lst[0]].append((lst[i], lst[i + 1]))


def dfs(v, weight):
    dist[v] = 0  # visited
    for i, w in tree[v]:
        if dist[i] != 0:
            dfs(i, weight + w)
    dist[v] = weight


dist = [-1] * (V + 1)
dfs(1, 0)
mid = dist.index(max(dist))

dist = [-1] * (V + 1)
dfs(mid, 0)
print(max(dist))
