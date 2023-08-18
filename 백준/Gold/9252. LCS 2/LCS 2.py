import sys

input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()
dp = [[0] * (len(s1) + 1) for _ in range(len(s2) + 1)]

for i in range(1, len(s2) + 1):
    for j in range(1, len(s1) + 1):
        if s2[i - 1] == s1[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            continue

        dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

lcsLen = dp[len(s2)][len(s1)]

lcs = []
maxLen = lcsLen
yPos, xPos = len(s2), len(s1)

while yPos > 0 and xPos > 0:
    if dp[yPos - 1][xPos] == maxLen:
        yPos -= 1
        continue
    if dp[yPos][xPos - 1] == maxLen:
        xPos -= 1
        continue

    yPos, xPos = yPos - 1, xPos - 1
    lcs.append(s2[yPos])
    maxLen = dp[yPos][xPos]

print(lcsLen)
if lcsLen > 0:
    print("".join(reversed(lcs)))
