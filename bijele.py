
# https://open.kattis.com/problems/bijele

pieces = input()

K = 1 - int(pieces[0])
Q = 1 - int(pieces[2])
R = 2 - int(pieces[4])
B = 2 - int(pieces[6])
N = 2 - int(pieces[8])
p = 8 - int(pieces[10])

print(f"{K} {Q} {R} {B} {N} {p}")
