import sys

input = sys.stdin.readline


def isTriangle(a, b, c):
    arr = sorted([a, b, c])
    return arr[0] + arr[1] > arr[2]


while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break

    if not isTriangle(a, b, c):
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a == b or b == c or c == a:
        print("Isosceles")
    else:
        print("Scalene")
