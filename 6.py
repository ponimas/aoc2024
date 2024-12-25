#! /usr/bin/env python3
from collections import defaultdict, namedtuple
from copy import deepcopy
from pprint import pprint

f = "test.6.txt"
f = "6.txt"

none = lambda: None
lab = defaultdict(lambda: defaultdict(none))

point = namedtuple("point", ["x", "y"])

r = open(f).readlines()
sz = (len(r[0].strip()) - 1, len(r) - 1)

for y, l in enumerate(r):
    for x, p in enumerate(l.strip()):
        if p == "#":
            lab[x][y] = "#"
            continue
        if p != ".":
            pos = point(x, y)
            g = p
        lab[x][y] = p


deltas = {">": (1, 0), "<": (-1, 0), "^": (0, -1), "v": (0, 1)}
turns = {">": "v", "<": "^", "^": ">", "v": "<"}

visited = set()

p = pos
d = g

visited.add((p, g))

while True:
    delta = deltas[d]
    lab[p.x][p.y] = d

    nx = p.x + delta[0]
    ny = p.y + delta[1]
    nxt = lab[nx][ny]

    if nxt == "#":
        d = turns[d]
        continue

    if nxt is None:
        break

    p = point(nx, ny)
    visited.add((p, d))

print(len({x for x, y in visited}))

p = pos
d = g
c = 0


def print_field(f, o=None):
    for y in range(sz[1] + 1):
        l = ""
        for x in range(sz[0] + 1):
            p = f[x][y]
            if o is not None and x == o.x and y == o.y:
                l += "O"
            else:
                l += p
        print(l)


# print_field(lab)


def detect_cycle(obst):
    lab_x = deepcopy(lab)
    visited_x = set()

    lab_x[obst.x][obst.y] = "#"

    d = g
    p = pos

    while True:
        # print_field(lab_x)
        # print()

        lab_x[p.x][p.y] = d
        delta = deltas[d]

        nx = p.x + delta[0]
        ny = p.y + delta[1]
        nxt = lab_x[nx][ny]

        if nxt == "#":
            d = turns[d]
            # print('turn', d, o)
            continue

        if nxt is None:
            break

        p = point(nx, ny)

        if (p, d) in visited_x:
            return obst
        visited_x.add((p, d))


visited = set()

p = pos
d = g

visited.add((p, g))

s = set()
while True:
    delta = deltas[d]

    lab[p.x][p.y] = d

    nx = p.x + delta[0]
    ny = p.y + delta[1]
    nxt = lab[nx][ny]

    if nxt == "#":
        d = turns[d]
        continue

    if nxt is None:
        break

    old_p = p
    p = point(nx, ny)

    if x := detect_cycle(p):
        s.add(x)
    visited.add((p, d))

pprint(len(s))


# print(c)
