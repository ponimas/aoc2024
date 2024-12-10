#!/usr/bin/env python3
from copy import deepcopy

f = 'test.9.txt'
# f = "9.txt"

m = []
for i, x in enumerate(open(f).readline().strip()):
    sz = int(x)
    m += ['.' if i % 2 else i // 2] * sz

mm = deepcopy(m)

l = 0
r = len(m) - 1

while True:
    if l == r:
        break
    if m[r] == '.':
        r -= 1
        continue
    if m[l] == '.':
        m[l], m[r] = m[r], m[l]
    l += 1

s = 0
for i, x in enumerate(m):
    if x != '.':
        s += i * int(x)
        # print(i, int(x), i * int(x), s)
print(s)

# m = []
# for k, g in groupby(mm):
#     g = list(g)
#     m.append(len(g), k)

# l = 0
# r = len(m) - 1
# while True:
#     if l == r:
#         break
#     if m[r][1] == '.':
#         r -= 1
#         continue
#     if m[l][1] == '.':
#         if
#         m[l], m[r] = m[r], m[l]
#     l += 1
