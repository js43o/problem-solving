import sys
from itertools import combinations

input = sys.stdin.readline


def getScore(s1, s2):
    score = 0
    for i in range(4):
        if s1[i] != s2[i]:
            score += 1
    return score


T = int(input())
for _ in range(T):
    N = int(input())
    arr = input().rstrip().split(" ")
    cnt = {}
    lst = []
    for mbti in arr:
        if mbti not in cnt:
            cnt[mbti] = 0
        if cnt[mbti] < 3:
            cnt[mbti] += 1
            lst.append(mbti)
    lst.sort()
    res = 10**9

    for a, b, c in combinations(lst, 3):
        res = min(
            res,
            getScore(a, b) + getScore(b, c) + getScore(c, a),
        )
    print(res)
