import sys

input = sys.stdin.readline

N, M = map(int, input().split())
edges = []
parent = [i for i in range(N + 1)]
res = 0


def find_parent(v):
    if parent[v] == v:
        return v
    parent[v] = find_parent(parent[v])  # 조상 찾고 다시 내려가면서 쭉 할당
    return parent[v]


def union_parent(v, w):
    if w > v:
        v, w = w, v

    v_parent = find_parent(v)
    w_parent = find_parent(w)
    parent[w_parent] = v_parent  # 조상 덮어쓰기


for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))

edges.sort()

lastCost = 0
for edge in edges:
    C, A, B = edge
    if find_parent(A) == find_parent(B):
        continue
    union_parent(A, B)
    res += C
    lastCost = C

print(res - lastCost)
