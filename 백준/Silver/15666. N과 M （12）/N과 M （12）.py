N, M = map(int, input().split())
arr = sorted(list(set(map(int, input().split()))))


def dfs(v, res):
    if len(res) == M:
        print(*res)
        return
    for i in arr:
        if i >= v:
            res.append(i)
            dfs(i, res)
            res.pop()


for i in arr:
    dfs(i, [i])
