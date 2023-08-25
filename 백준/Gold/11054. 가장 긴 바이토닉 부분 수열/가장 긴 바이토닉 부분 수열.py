n = int(input())
arr = list(map(int, input().split()))
asc = [1] * n
desc = [1] * n

for i in range(n):
    m = 0
    for j in range(i):
        if arr[i] > arr[j]:
            m = max(m, asc[j])
    asc[i] = m + 1


for i in range(n - 1, -1, -1):
    m = 0
    for j in range(n - 1, i, -1):
        if arr[i] > arr[j]:
            m = max(m, desc[j])
    desc[i] = m + 1

for i in range(n):
    asc[i] += desc[i] - 1

print(max(asc))