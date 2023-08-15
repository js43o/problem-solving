import sys

input = sys.stdin.readline

s = input().rstrip()
flag = 1

for i in range(len(s) // 2):
    if s[i] != s[-(1 + i)]:
        flag = 0
        break

print(flag)
