n, k = map(int, input().split())
arr = [i for i in range(1, n + 1)]
removed = []
index = 0

while len(arr) > 1:
    index += k - 1
    if index >= len(arr):
        index %= len(arr)
    removed.append(str(arr[index]))
    arr.remove(arr[index])

removed.append(str(arr[0]))
print("<%s>" % ", ".join(removed))
