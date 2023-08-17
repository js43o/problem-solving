n = int(input())

i0 = 3
i1 = 2
i2 = 1

if n <= 3:
    print(n)
else:
    for _ in range(4, n + 1):
        i2 = i1
        i1 = i0
        i0 = (i1 + i2) % 15746

    print(i0)
