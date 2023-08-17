import sys

sys.setrecursionlimit(10**8)

n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

pos = [-1] * (n + 1)
for i in range(n):
    pos[in_order[i]] = i  # 인오더에서 각 원소가 등장한 인덱스 기록


def go(in_start, in_end, post_start, post_end):
    if (in_start > in_end) or (post_start > post_end):
        return

    root = post_order[post_end]
    left_size = pos[root] - in_start

    print(root, end=" ")
    go(in_start, pos[root] - 1, post_start, post_start + left_size - 1)
    go(pos[root] + 1, in_end, post_start + left_size, post_end - 1)


go(0, n - 1, 0, n - 1)
