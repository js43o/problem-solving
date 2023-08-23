L = int(input())
str = input()

res = 0
R = 31
M = 1234567891
for i in range(L):
    res += (ord(str[i]) - ord("a") + 1) * (R ** i) % M

print(res % M)
