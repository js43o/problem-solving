from collections import deque
import sys

graph = [set() for _ in range(1001)]
result_dfs = []
result_bfs = []

N, M, V = map(int, sys.stdin.readline().split())
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].add(b)
    graph[b].add(a)


def dfs(v, visited):
    visited.append(v)
    result_dfs.append(str(v))

    lst = list(graph[v])
    lst.sort()
    for i in lst:
        if i not in visited:
            dfs(i, visited)


def bfs(init):
    queue = deque([init])
    visited = []

    while queue:
        v = queue.popleft()

        if v not in visited:
            visited.append(v)
            result_bfs.append(str(v))

            lst = list(graph[v])
            lst.sort()
            queue.extend(lst)


dfs(V, [])
bfs(V)

print(" ".join(result_dfs))
print(" ".join(result_bfs))
