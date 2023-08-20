n = int(input())
arr = list(map(int, input().split()))
v = int(input())

result = 0
for a in arr:
  if v == a:
    result += 1
print(result)