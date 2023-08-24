import sys

input = sys.stdin.readline

N, M = map(int, input().split())
in_node = [[False] * (N + 1) for _ in range(N + 1)]
out_node = [[False] * (N + 1) for _ in range(N + 1)]
in_counter = [0] * (N + 1)
res = []

for _ in range(M):
    arr = list(map(int, input().split()))[1:]
    for i in range(1, len(arr)):  # arr[i - 1] -> arr[i]
        if not in_node[arr[i]][arr[i - 1]]:
            in_counter[arr[i]] += 1  # 중복된 경로가 아닐 때에만 카운트
        in_node[arr[i]][arr[i - 1]] = True
        out_node[arr[i - 1]][arr[i]] = True

for i in range(N):  # 총 N번 반복
    v = None
    for j in range(1, N + 1):
        if in_counter[j] == 0:  # IN이 없는(= 최상단의) 노드를 선택
            v = j
            in_counter[j] -= 1  # 중복 방문하지 않도록 -1로 설정
            break

    if not v:  # 사이클이 있는 경우 IN == 0인 노드가 존재하지 않게 됨
        break
    res.append(v)

    for k in range(1, N + 1):  # 해당 노드와 연결된 모든 OUT 엣지를 제거
        if out_node[v][k]:
            out_node[v][k] = False
            in_node[k][v] = False
            in_counter[k] -= 1


if len(res) < N:
    print(0)
else:
    for r in res:
        print(r)
