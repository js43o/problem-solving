import sys

graph = {}
N = int(input())
E = int(input())

for _ in range(E):
    a, b = map(int, sys.stdin.readline().split())
    if not a in graph:
        graph[a] = []
    if not b in graph:
        graph[b] = []
    graph[a].append(b)
    graph[b].append(a)


count = 0
visited = []


def dfs(v):
    global graph
    global count
    global visited
    count += 1
    visited.append(v)
    if not v in graph:
        return
    for i in graph[v]:
        if i not in visited:
            dfs(i)


dfs(1)
print(count - 1)
