a, b = list((map(int, input().split())))

gcd = 0
lcm = 0

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

print(gcd)

a_ = a
b_ = b

while 1:
    if a_ == b_:
        lcm = a_
        break
    elif a_ < b_:
        a_ += a
    elif a_ > b_:
        b_ += b

print(lcm)
