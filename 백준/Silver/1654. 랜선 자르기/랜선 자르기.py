from sys import stdin

k, n = map(int, input().split())
arr = [int(stdin.readline()) for _ in range(k)]
min_len, max_len = 1, max(arr)

while min_len <= max_len:
    cur_len = (min_len + max_len) // 2
    count = 0
    for i in arr:
        count += i // cur_len
    if count >= n:
        min_len = cur_len + 1
    else:
        max_len = cur_len - 1

print(max_len)
