import sys

input = sys.stdin.readline

mat = [[False] * 100 for _ in range(100)]
count = 0

N = int(input())
for _ in range(N):
    left, bottom = map(int, input().split())
    for i in range(left, left + 10):
        for j in range(bottom, bottom + 10):
            if not mat[i][j]:  # 처음 붙이게 되었을 때
                count += 1
            mat[i][j] = True

print(count)
