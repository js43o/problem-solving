import sys

N = int(input())
arr = []

for _ in range(N):
    s, e = map(int, sys.stdin.readline().split())
    arr.append({"start": s, "end": e})

arr.sort(key=lambda x: (x["end"], x["start"]))

count = 1
v = arr[0]["end"]
for i in range(1, N):
    if arr[i]["start"] >= v:
        count += 1
        v = arr[i]["end"]


print(count)
