num = []
oper = []
s = "(" + input().rstrip() + ")"


for i in range(0, len(s)):
    if "A" <= s[i] <= "Z":
        num.append(s[i])
        if oper and len(num) >= 2:
            top = oper[len(oper) - 1]
            if top == "*" or top == "/":
                temp = num.pop()
                num.append(num.pop() + temp + oper.pop())  # 즉시 한 번 연산
    else:
        if s[i] == "+" or s[i] == "-":
            while oper and len(num) >= 2:
                top = oper[len(oper) - 1]
                if top == "(":
                    break
                temp = num.pop()
                num.append(num.pop() + temp + oper.pop())  # '('을 만날 때까지 계속 연산
            oper.append(s[i])
        elif s[i] == ")":
            while oper and len(num) >= 2:
                top = oper[len(oper) - 1]
                if top == "(":
                    oper.pop()
                    break
                temp = num.pop()
                num.append(num.pop() + temp + oper.pop())  # '('을 만날 때까지 계속 연산

            top = oper[len(oper) - 1]
            if top == "*" or top == "/":  # 괄호를 처리했을 때 연산자가 앞에 남아있다면
                temp = num.pop()
                num.append(num.pop() + temp + oper.pop())  # 추가로 한 번 더 연산
        else:
            oper.append(s[i])


while oper and len(num) >= 2:
    temp = num.pop()
    num.append(num.pop() + temp + oper.pop())

print(num.pop())
