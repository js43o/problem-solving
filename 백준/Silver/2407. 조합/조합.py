n, r = map(int, input().split())
a = 1
b = 1
for _ in range(r):
    a *= n
    n -= 1
for i in range(2, r + 1):
    b *= i

print(a // b)
