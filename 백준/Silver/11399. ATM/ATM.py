from functools import reduce

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

for i in range(1, len(arr)):
    arr[i] = arr[i] + arr[i - 1]

print(reduce(lambda acc, cur: acc + cur, arr))
