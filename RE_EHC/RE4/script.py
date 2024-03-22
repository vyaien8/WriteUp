# opcode 49 in 6502 is Xor operator
# the last character of flag is '}'
# => xor value = ord('}') ^ 117 = 8
flag = [75, 92, 78, 100, 109, 105, 122, 102, 115, 96, 56, 101, 59, 87, 107, 56, 101, 120, 125, 124, 59, 122, 87, 122, 59, 126, 56, 100, 125, 124, 57, 56, 102, 117]
for c in flag:
    print(chr(c ^ 8))