import sys

input = sys.stdin.readline

N = int(input())
students = []
favorite = {}
mat = [[0] * (N + 1) for _ in range(N + 1)]
res = 0


def getMostFavoritePos(favoriteList):
    favoriteScoreList = []
    for y in range(1, N + 1):
        for x in range(1, N + 1):
            if mat[y][x] != 0:  # 현재 자리가 비어있지 않으면 패스
                continue
            curScore = [0, 0, -y, -x]
            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if 1 <= y + dy <= N and 1 <= x + dx <= N:
                    if mat[y + dy][x + dx] in favoriteList:  # 인접한 칸에 친한 친구가 있을 때
                        curScore[0] += 1
                    elif mat[y + dy][x + dx] == 0:  # 비어있을 때
                        curScore[1] += 1
            favoriteScoreList.append(curScore)

    return list(sorted(favoriteScoreList, reverse=True))[0]


for _ in range(N**2):
    arr = list(map(int, input().split(" ")))
    students.append(arr[0])
    favorite[arr[0]] = arr[1:]


for student in students:
    pos = getMostFavoritePos(favorite[student])
    favoriteScore, emptyScore, y, x = pos
    y, x = -y, -x
    mat[y][x] = student

for y in range(1, N + 1):
    for x in range(1, N + 1):
        favoriteCount = 0
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 1 <= y + dy <= N and 1 <= x + dx <= N:
                if mat[y + dy][x + dx] in favorite[mat[y][x]]:  # 인접한 칸에 친한 친구가 있을 때
                    favoriteCount += 1
        if favoriteCount > 0:
            res += 10 ** (favoriteCount - 1)

print(res)
