s = input()
score = 0.0
if s[0] == "A":
    score += 4
elif s[0] == "B":
    score += 3
elif s[0] == "C":
    score += 2
elif s[0] == "D":
    score += 1

if s[0] != 'F' and s[1] == "+":
    score += 0.3
elif s[0] != 'F' and s[1] == "-":
    score -= 0.3
print(score)
