import sys
import heapq

input = sys.stdin.readline


V, E = map(int, input().split())
edges = []
parent = [i for i in range(V + 1)]
res = 0


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(x, y):
    x = find_parent(x)
    y = find_parent(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


for _ in range(E):
    A, B, C = map(int, input().split())
    heapq.heappush(edges, (C, A, B))

while edges:
    C, A, B = heapq.heappop(edges)

    if find_parent(A) != find_parent(B):
        union_parent(A, B)
        res += C

print(res)
