import sys

input = sys.stdin.readline

code = {
    "ADD": "0000",
    "SUB": "0001",
    "MOV": "0010",
    "AND": "0011",
    "OR": "0100",
    "NOT": "0101",
    "MULT": "0110",
    "LSFTL": "0111",
    "LSFTR": "1000",
    "ASFTR": "1001",
    "RL": "1010",
    "RR": "1011",
}

N = int(input())
for i in range(N):
    opcode, rd, ra, rb = input().split()
    codeNum = ""
    if opcode[-1] == "C":
        codeNum = code[opcode[:-1]] + "10"
    else:
        codeNum = code[opcode] + "00"
    if codeNum[4] == "0":
        rb = bin(int(rb))[2:].zfill(3) + "0"
    else:
        rb = bin(int(rb))[2:].zfill(4)
    print(
        "%s%s%s%s"
        % (
            codeNum,
            bin(int(rd))[2:].zfill(3),
            bin(int(ra))[2:].zfill(3),
            rb,
        )
    )
