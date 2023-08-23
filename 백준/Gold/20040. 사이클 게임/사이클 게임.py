import sys

input = sys.stdin.readline


n, m = map(int, input().split())
parent = list(range(n))
res = 0


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a == b:
        return False

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

    return True


for i in range(1, m + 1):
    a, b = map(int, input().split())
    if not union_parent(a, b) and res == 0:
        res = i

print(res)
