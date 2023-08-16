import sys

input = sys.stdin.readline

N = int(input())
words = [input().rstrip() for _ in range(N)]
words.sort(key=len)
res = 0

for i in range(N):
    flag = True
    for j in range(i + 1, N):
        if words[i] == words[j][0 : len(words[i])]:  # 접두사 확인
            flag = False
            break

    if flag:
        res += 1

print(res)
