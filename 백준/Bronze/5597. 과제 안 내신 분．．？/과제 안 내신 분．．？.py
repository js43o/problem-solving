arr = [False] * 30
for _ in range(28):
    i = int(input())
    arr[i - 1] = True

for i in range(len(arr)):
    if not arr[i]:
        print(i + 1)
