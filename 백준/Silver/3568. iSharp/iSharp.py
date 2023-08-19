import sys

input = sys.stdin.readline

s = input().split()
defaultType = s[0]
result = []
typeSymbol = set(["&", "*", "["])

for a in s[1:]:
    idx = 0
    while idx < len(a):
        if a[idx] in typeSymbol:
            break
        idx += 1
    if idx == len(a):
        result.append("%s %s;" % (defaultType, a[:-1]))
        continue
    newType = defaultType
    for i in range(len(a) - 2, idx - 1, -1):
        if a[i] == "]":
            newType += "[]"
            continue
        if a[i] == "[":
            continue
        newType += a[i]

    result.append("%s %s;" % (newType, a[:idx]))

print("\n".join(result))
