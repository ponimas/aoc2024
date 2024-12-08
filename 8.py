#! /usr/bin/env python3
from collections import defaultdict, namedtuple
from itertools import combinations

f = 'test.txt'
f = '8.txt'
# m = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: None)))

m = defaultdict(list)
point = namedtuple('point', ['x', 'y'])

max_x, max_y = 0, 0

for y, l in enumerate(open(f)):
    for x, p in enumerate(l.strip()):
        max_x, max_y = x, y
        if p != '.':
            m[p].append(point(x, y))


def mk_antenas(a, b):
    diff_x = a.x - b.x
    diff_y = a.y - b.y
    for k in [point(a.x + diff_x, a.y + diff_y), point(b.x - diff_x, b.y - diff_y)]:
        if k.x >= 0 and k.x <= max_x and k.y >= 0 and k.y <= max_y:
            yield k


antinodes = set()
for l, ps in m.items():
    l = len(antinodes)
    for a, b in combinations(ps, 2):
        for i in mk_antenas(a, b):
            antinodes.add(i)


print(len(antinodes))


def mk_antenas_2(a, b):
    diff_x = a.x - b.x
    diff_y = a.y - b.y

    k = a
    l = b

    while True:
        k = point(k.x + diff_x, k.y + diff_y)
        if k.x >= 0 and k.x <= max_x and k.y >= 0 and k.y <= max_y:
            yield k
        else:
            break

    while True:
        l = point(l.x - diff_x, l.y - diff_y)
        if l.x >= 0 and l.x <= max_x and l.y >= 0 and l.y <= max_y:
            yield l
        else:
            break


antinodes = set()
for l, ps in m.items():
    l = len(antinodes)
    for a, b in combinations(ps, 2):
        antinodes.add(a)
        antinodes.add(b)
        for i in mk_antenas_2(a, b):
            antinodes.add(i)

print(len(antinodes))
