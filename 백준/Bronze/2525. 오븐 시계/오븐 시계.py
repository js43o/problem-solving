import sys

input = sys.stdin.readline

A, B = map(int, input().split())
C = int(input())

total = A * 60 + B + C
hours = (total // 60) % 24
minutes = total % 60

print("%d %d" % (hours, minutes))
