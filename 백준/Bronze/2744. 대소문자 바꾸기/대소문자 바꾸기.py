s = input()
for a in s:
    if a.isupper():
        print(a.lower(), end="")
    else:
        print(a.upper(), end="")
