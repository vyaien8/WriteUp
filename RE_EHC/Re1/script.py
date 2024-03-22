from z3 import *
cipher = [517, 223, 357, 514, 662, 468, 570, 210, 357, 532, 776, 573, 474, 76, 250, 311, 708, 797, 407, 252, 304, 566, 696, 634, 594, 224, 391, 606, 762, 645, 313, 154, 285, 288, 450, 543]
v11 = [1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1]
xorArray = [0x000000F7, 0x000000DA, 0x000000AF, 0x00000052, 0x00000079, 0x000000E4, 0x0000002F, 0x000000B2, 0x00000088, 0x00000003, 0x00000036, 0x00000095, 0x0000004B, 0x000000E4, 0x00000015, 0x000000E5, 0x000000AD, 0x00000088, 0x000000DB, 0x00000023, 0x00000092, 0x000000FB, 0x000000FA, 0x0000001D, 0x000000EE, 0x000000CD, 0x000000A2, 0x00000027, 0x0000001D, 0x00000080, 0x00000068, 0x0000004C, 0x000000DC, 0x000000A4, 0x0000004D, 0x000000F8]
phakeinput = "123456789012345678901234567890123456"
for i in range(len(xorArray)):
    xorArray[i] ^= ord(phakeinput[i])

v12 = [BitVec(f'{i:2}', 8) for i in range(36)]
s = Solver()
x = [0]*36
for i in range(6):
    for j in range(6):
        for k in range(6):
            x[i* 6 + j] += v12[6*i + k] * v11[6*k + j]

for i, j in zip(x, cipher):
    s.add(i == j)
s.check()
m = s.model()
model = sorted([(d, m[d]) for d in m], key = lambda x: str(x[0]))
i = 0
for m in model:
    print(chr((m[1].as_long()) ^ xorArray[i]), end = '')
    i += 1
# EHC{y0u_c4n_s0lv3_1t_w1th0ut_d3bug!}