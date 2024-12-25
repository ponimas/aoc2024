#!/usr/bin/env python3
from collections import deque, defaultdict
from pyrsistent import v, s
from itertools import groupby


f = 'test.20.txt'
f = '20.input.txt'

m = defaultdict(lambda: None)

for y, l in enumerate(open(f)):
    for x, p in enumerate(l.strip()):
        i = x + y * 1j
        m[i] = p
        if p == 'S':
            start = i
        elif p == 'E':
            end = i

deltas = [-1, 1, -1j, 1j]
q = deque([v(start)])


visited = set()
while len(q):
    pth = q.popleft()
    p = pth[-1]
    if p == end:
        path = pth
        break

    for d in deltas:
        np = p + d
        if np not in m or np in visited or m[np] == '#':
            continue

        visited.add(np)
        q.append(pth.append(np))

ddeltas = [-2, 2, -2j, 2j]
cuts = set()

for p in visited:
    for d, dd in zip(deltas, ddeltas):
        if m[p + d] == '#' and p + dd in visited:
            cuts.add(s(p, p + dd))
print(len(cuts))


def dist(s):
    s, e = list(s)
    return abs(path.index(e) - path.index(s))


cuts = sorted(cuts, key=dist)
a = 0
for l, c in groupby(cuts, dist):
    if l >= 102:
        a += len(list(c))

print(a)

# ddeltas = [-20, 20, -20j, 20j]
# cuts = set()

# for p in visited:
#     for d, dd in zip(deltas, ddeltas):
#         if m[p + d] == '#' and p + dd in visited:
#             cuts.add(s(p, p + dd))

# print(len(cuts))


# def l(s):
#     s, e = list(s)
#     return abs(path.index(e) - path.index(s))


# cuts = sorted(cuts, key=l)
# a = 0
# for l, c in groupby(cuts, l):
#     if l >= 102:
#         a += len(list(c))

# print(a)
