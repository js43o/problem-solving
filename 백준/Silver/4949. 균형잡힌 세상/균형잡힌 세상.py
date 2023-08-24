import sys


def last(arr):
    return arr[len(arr) - 1] if len(arr) > 0 else -1


while True:
    str = sys.stdin.readline().rstrip()
    stack = []
    isBalanced = True
    if str == ".":
        break
    for c in str:
        if c == "(" or c == "[":
            stack.append(c)
        elif c == ")":
            if last(stack) == "(":
                stack.pop()
            else:
                isBalanced = False
                break
        elif c == "]":
            if last(stack) == "[":
                stack.pop()
            else:
                isBalanced = False
                break
    if isBalanced and len(stack) == 0:
        print("yes")
    else:
        print("no")
