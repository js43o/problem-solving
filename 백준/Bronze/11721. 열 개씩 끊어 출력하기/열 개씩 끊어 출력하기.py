n = input()
count = 10

while count <= len(n) + 10:
    if len(n) - count >= 0:
        for i in range(count - 10, count):
            print(n[i], end='')
    else:
        for i in range(count - 10, len(n)):
            print(n[i], end='')
        break
    print('')
    count += 10