N, M = map(int, input().split())
arr = list(map(int, input().split()))

max_h = max(arr)
min_h = 0

while max_h >= min_h:
    mid = (max_h + min_h) // 2
    length = sum(i - mid if i > mid else 0 for i in arr)
    if length >= M:
        min_h = mid + 1
    else:
        max_h = mid - 1

print(max_h)
