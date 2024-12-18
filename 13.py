#!/usr/bin/env python3
import re
import heapq

f = 'test.txt'
# f= '13.txt'

rx = r'.+X\+(?P<xa>\d+), Y\+(?P<ya>\d+)\n.+X\+(?P<xb>\d+), Y\+(?P<yb>\d+)\nPrize: X=(?P<xp>\d+), Y=(?P<yp>\d+)'

with open(f) as f:
    machines = [
        {k: int(v) for (k, v) in p.groupdict().items()}
        for p in re.finditer(rx, f.read(), re.MULTILINE)
    ]

spent = 0
for machine in machines:
    xa, ya = (machine['xa'], machine['ya'])
    xb, yb = (machine['xb'], machine['yb'])
    xp, yp = (machine['xp'], machine['yp'])

    p = (0, 0)
    q = [(0, p)]

    visited = set()
    while len(q):
        c, (x, y) = heapq.heappop(q)
        if (x, y) in visited:
            continue
        if x == xp and y == yp:
            spent += c
            break

        if x > xp or y > yp:
            continue

        visited.add((x, y))
        da = (x + xa, y + ya)
        db = (x + xb, y + yb)
        heapq.heappush(q, (c + 3, da))
        heapq.heappush(q, (c + 1, db))

print(spent)

for machine in machines:
    xa, ya = (machine['xa'], machine['ya'])
    xb, yb = (machine['xb'], machine['yb'])
    xp, yp = (machine['xp'], machine['yp'])
    mx = min([xa, xb])
    my = min([xa, xb])
