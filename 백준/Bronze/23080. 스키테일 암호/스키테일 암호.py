import sys

input = sys.stdin.readline

n = int(input().rstrip())
s = input().rstrip()
idx = 0

while idx < len(s):
    print(s[idx], end="")
    idx += n
