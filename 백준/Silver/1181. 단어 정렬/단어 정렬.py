n = int(input())
list_input = [list(input()) for _ in range(n)]


def merge_sort(list):
    length = len(list)
    if length <= 1:
        return list
    m = int(length / 2)
    l = list[:m]
    r = list[m:]
    return merge(merge_sort(l), merge_sort(r))


def merge(l, r):
    i = j = 0
    result = []
    while i < len(l) and j < len(r):
        if compare(l[i], r[j]) == r[j]:
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


def compare(a, b):
    if len(a) > len(b):
        return a
    elif len(a) < len(b):
        return b
    else:
        for k in range(len(a)):
            if a[k] > b[k]:
                return a
            elif a[k] < b[k]:
                return b
        return a  # a == b


def join_chars(list):
    return "".join(list)


prev = ""
for i in list(map(join_chars, merge_sort(list_input))):
    if i == prev:
        continue
    print(i)
    prev = i
