import sys

sys.setrecursionlimit(10 ** 9)

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(vertex):
    global graph
    global visited

    visited[vertex] = True

    for i in graph[vertex]:
        if not visited[i]:
            dfs(i)


count = 0

for i in range(1, len(visited)):
    if visited[i] == False:
        count += 1
        dfs(i)

print(count)
