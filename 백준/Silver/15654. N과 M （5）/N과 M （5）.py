N, M = map(int, input().split())
arr = sorted(list(set(map(int, input().split()))))


def dfs(res):
    if len(res) == M:
        print(*res)
        return
    for i in arr:
        if i not in res:
            res.append(i)
            dfs(res)
            res.pop()


for i in arr:
    dfs([i])
