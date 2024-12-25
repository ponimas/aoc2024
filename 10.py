#!/usr/bin/env python3

from collections import defaultdict, namedtuple, deque
from copy import copy

f = "test.txt"
f = "10.txt"

m = defaultdict(lambda: defaultdict(lambda: -1))
heads = []
point = namedtuple("point", ["x", "y"])


for y, l in enumerate(open(f)):
    for x, p in enumerate(l.strip()):
        if p == ".":
            p = -1
        else:
            p = int(p)
        if p == 0:
            heads.append(point(x, y))
        m[x][y] = p

deltas = [point(-1, 0), point(1, 0), point(0, -1), point(0, 1)]


def search(start):
    visited = set()
    pos = start
    q = deque([[pos]])
    while len(q) > 0:
        path = q.popleft()
        pos = path[-1]

        v = m[pos.x][pos.y]
        for d in deltas:
            pth = copy(path)
            n = point(pos.x + d.x, pos.y + d.y)

            vn = m[n.x][n.y]
            if vn - v != 1:
                continue
            pth.append(n)
            if vn == 9:
                visited.add(tuple(pth))
            else:
                q.append(pth)
    return visited


s = 0
ss = 0

for p in heads:
    paths = search(p)
    s += len({p[-1] for p in paths})
    ss += len(paths)

print(s, ss)
