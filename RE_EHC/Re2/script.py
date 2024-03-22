from z3 import *
v5  = [1,3,3,7,222,173,190,239] # xor with input
# shuffer: even into odd, odd into even
cipher = [ 0x57 ,0x42 ,0x4b, 0x45 ,0xCC ,0xBB,0x81,0xCC,0x71,0x7A,0x71,0x66,0xDF,0xBB,0x86,0xCD,0x64,0x6F,0x6E,0x5C,0xF2,0xAD,0x9A,0xD8, 0x7e, 0x6f]

flag = [BitVec(f'{i:2}', 8) for i in range(len(cipher))]
s = Solver()
# for f in flag:
#     s.add(f > 0x20, f <= 0x7f)

for i in range(len(flag)):
    flag[i] ^= v5[i%8]
x = [0] * len(cipher)
print(len(x))
for i in range(0, len(cipher), 2):
    x[i] = flag[i + 1]
for j in range(1, len(cipher), 2):
    x[j] = flag[j - 1]
for i, j in zip(x, cipher):
    s.add(i == j)
print(s.check())
m = s.model()
model = sorted([(d, m[d]) for d in m], key = lambda x: str(x[0]))
for m in model:
     print(chr(m[1].as_long()), end='')
# CTFLearn{reversing_is_fun}