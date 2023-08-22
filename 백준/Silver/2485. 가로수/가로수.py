import sys, math

input = sys.stdin.readline

N = int(input())
trees = []
dist = []
result = 0

for _ in range(N):
    trees.append(int(input()))

for i in range(len(trees) - 1):
    dist.append(trees[i + 1] - trees[i])

standards = (trees[-1] - trees[0]) // math.gcd(*dist) + 1
print(standards - len(trees))
