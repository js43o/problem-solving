N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))


def dfs(v, res, count):
    if count == M:
        print(*res)
        return
    for i in arr:
        if i >= v:
            res.append(i)
            dfs(i, res, count + 1)
            res.pop()


for i in arr:
    dfs(i, [i], 1)
