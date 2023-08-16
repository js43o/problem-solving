import math

N = int(input())
f = str(math.factorial(N))
count = 0

for i in f[::-1]:
    if i == "0":
        count += 1
    else:
        print(count)
        break
