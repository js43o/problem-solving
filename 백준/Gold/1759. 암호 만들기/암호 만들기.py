import sys

input = sys.stdin.readline

L, C = map(int, input().split())
arr = input().rstrip().split(" ")
VOWEL = set(["a", "e", "i", "o", "u"])

arr.sort()


def dfs(idx, res, consonant, vowel):
    if len(res) == L and consonant >= 2 and vowel >= 1:
        print("".join(res))
        return

    for i in range(idx + 1, len(arr)):
        dfs(
            i,
            [*res, arr[i]],
            consonant + (1 if arr[i] not in VOWEL else 0),
            vowel + (1 if arr[i] in VOWEL else 0),
        )


for i in range(0, C - L + 1):
    dfs(i, [arr[i]], 1 if arr[i] not in VOWEL else 0, 1 if arr[i] in VOWEL else 0)
