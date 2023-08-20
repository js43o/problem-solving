import sys

input = sys.stdin.readline

K = int(input())
tree = [0] * (2**K)
buildings = list(map(int, input().split(" ")))
curBuildingIdx = 0


def traversal(idx):
    global curBuildingIdx

    if idx >= 2**K:
        return
    traversal(idx * 2)
    tree[idx] = buildings[curBuildingIdx]
    curBuildingIdx += 1
    traversal(idx * 2 + 1)


traversal(1)

for level in range(1, K + 1):
    for i in range(2 ** (level - 1), 2**level):
        print(tree[i], end=" ")
    print()
