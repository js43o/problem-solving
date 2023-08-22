import sys
n = int(sys.stdin.readline().rstrip())
l = []

for i in range(n):
    a = sys.stdin.readline().rstrip()
    b = a.split(' ')
    l.append(int(b[0]) + int(b[1]))

for i in range(len(l)):
    print(l[i])