import sys

input = sys.stdin.readline

S = input().rstrip()
words = set()

for offset in range(1, len(S) + 1):
    for start in range(len(S)):
        if start + offset <= len(S):
            words.add(S[start : start + offset])

print(len(words))
