import sys, itertools

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    s = list(input().rstrip())
    a, b = -1, -1
    diff = 26
    for i in range(len(s) - 1, 0, -1):
        if s[i - 1] < s[i]:
            a = i - 1
            break

    if a == -1:
        print("".join(s))
        continue

    for i in range(a + 1, len(s)):
        if s[i] > s[a] and ord(s[i]) - ord(s[a]) < diff:
            b = i
            diff = ord(s[i]) - ord(s[a])

    s[a], s[b] = s[b], s[a]
    s = s[: a + 1] + sorted(s[a + 1 :])
    print("".join(s))
