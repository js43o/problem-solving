import sys

input = sys.stdin.readline

broken = [False] * 10
N = int(input())
M = int(input())
if M > 0:
    for i in list(map(int, input().split())):
        broken[i] = True
MAX = 0
MIN = 0
for i in range(9, -1, -1):
    if not broken[i]:
        MAX = i
        break
for i in range(1, 10, 1):
    if not broken[i]:
        MIN = i
        break


def count_channel():
    if N == 100:
        return 0
    if M == 10:
        return abs(N - 100)
    upper_bound = ""
    lower_bound = ""
    if not broken[0]:
        upper_bound = str(MIN) + "0" * len(str(N))
    else:
        upper_bound = str(MIN) * (len(str(N)) + 1)
    if len(str(N)) > 1:
        lower_bound = str(MAX) * (len(str(N)) - 1)
    else:
        lower_bound = "0" if not broken[0] else str(MIN)
    bound = min(
        len(upper_bound) + abs(N - int(upper_bound)),
        len(lower_bound) + abs(N - int(lower_bound)),
    )
    res_upper = ""
    res_lower = ""
    for d in str(N):
        if broken[int(d)]:
            break
        res_upper += d
        res_lower += d
    # 상한값
    idx = len(res_upper) if res_upper else 0
    flag = True
    while flag and 0 <= idx < len(str(N)):
        for i in range(int(str(N)[idx]) + 1, 10):
            if not broken[i]:
                res_upper = res_upper[:idx] + str(i)
                while len(res_upper) < len(str(N)):
                    res_upper += "0" if not broken[0] else str(MIN)
                flag = False
                break
        idx -= 1
    if not res_upper:
        if not broken[0]:
            res_upper = str(MIN) + "0" * len(str(N))
        else:
            res_upper = str(MIN) * (len(str(N)) + 1)
    # 하한값
    idx = len(res_lower) if res_lower else 0
    flag = True
    while flag and 0 <= idx < len(str(N)):
        for i in range(int(str(N)[idx]) - 1, -1, -1):
            if not broken[i]:
                res_lower = res_lower[:idx] + str(i)
                while len(res_lower) < len(str(N)):
                    res_lower += str(MAX)
                flag = False
                break
        idx -= 1
    if not res_lower:
        if len(str(N)) > 1:
            res_lower = str(MAX) * (len(str(N)) - 1)
        else:
            res_lower = "0" if not broken[0] else str(MIN)
    return min(
        abs(N - 100),
        bound,
        len(str(int(res_upper))) + abs(N - int(res_upper)),
        len(str(int(res_lower))) + abs(N - int(res_lower)),
    )


print(count_channel())
