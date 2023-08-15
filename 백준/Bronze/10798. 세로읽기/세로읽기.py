import sys

input = sys.stdin.readline

mat = [[" "] * 15 for _ in range(5)]

for i in range(5):
    word = input().rstrip()
    for j in range(len(word)):
        mat[i][j] = word[j]

for j in range(15):
    for i in range(5):
        if mat[i][j] == " ":
            continue
        print(mat[i][j], end="")
