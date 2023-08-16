import sys


def merge(l, r):
    i = j = 0
    result = []
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            result.append(l[i])
            i += 1
        elif l[i] >= r[j]:
            result.append(r[j])
            j += 1
    if i >= len(l):
        for k in range(j, len(r)):
            result.append(r[k])
    else:
        for k in range(i, len(l)):
            result.append(l[k])
    return result


def mergeSort(list):
    length = len(list)
    if length <= 1:
        return list
    m = int(length / 2)
    l = list[:m]
    r = list[m:]
    return merge(mergeSort(l), mergeSort(r))


n = int(input())
inputed = list(map(int, sys.stdin.readline().split()))
arr = mergeSort(list(set(inputed)))
dic = {arr[i]: i for i in range(len(arr))}

for i in inputed:
    print(dic[i], end=" ")
