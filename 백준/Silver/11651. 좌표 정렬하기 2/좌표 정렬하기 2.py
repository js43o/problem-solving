import sys


def merge(l, r):
    i = j = 0
    result = []
    while i < len(l) and j < len(r):
        if l[i]["y"] < r[j]["y"]:
            result.append(l[i])
            i += 1
        elif l[i]["y"] > r[j]["y"]:
            result.append(r[j])
            j += 1
        else:
            if l[i]["x"] <= r[j]["x"]:
                result.append(l[i])
                i += 1
            else:
                result.append(r[j])
                j += 1
    if i >= len(l):
        for k in range(j, len(r)):
            result.append(r[k])
    else:
        for k in range(i, len(l)):
            result.append(l[k])
    return result


def merge_sort(list):
    length = len(list)
    if length <= 1:
        return list
    m = int(length / 2)
    l = list[:m]
    r = list[m:]
    return merge(merge_sort(l), merge_sort(r))


n = int(input())
arr = []

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    arr.append({"x": a, "y": b})


def joinCoords(dict):
    return "%d %d" % (dict["x"], dict["y"])


for i in list(map(joinCoords, merge_sort(arr))):
    print(i)
