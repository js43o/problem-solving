import sys

N, M = map(int, input().split())
dic = {}

for _ in range(N):
    site, password = sys.stdin.readline().split()
    dic[site] = password

for _ in range(M):
    print(dic[sys.stdin.readline().rstrip()])
