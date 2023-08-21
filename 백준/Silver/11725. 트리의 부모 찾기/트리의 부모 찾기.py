import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input().rstrip())
tree = [[] for _ in range(N + 1)]
parent = [-1] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)


def dfs(v, p):
    parent[v] = 0  # visited
    for i in tree[v]:
        if parent[i] != 0:
            dfs(i, v)
    parent[v] = p


dfs(1, -1)
print(*parent[2:], sep="\n")
