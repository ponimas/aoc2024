#!/usr/bin/env python3.13
from heapq import heappush, heappop
from dataclasses import dataclass, field


f = 'test.txt'
f = '16.txt'


@dataclass(order=True)
class Item:
    score: int
    y: int = field(compare=False)
    x: int = field(compare=False)
    d: str = field(compare=False)
    # track: Any = field(compare=False)


m = open(f).readlines()

for y, l in enumerate(m):
    for x, c in enumerate(l):
        if c == 'S':
            pos = Item(0, y, x, 'E')
        if c == 'E':
            end = (y, x)
moves = {
    'E': [(0, 1, 'E'), (-1, 0, 'N'), (1, 0, 'S')],
    'W': [(-1, 0, 'N'), (0, -1, 'W'), (1, 0, 'S')],
    'N': [(0, 1, 'E'), (-1, 0, 'N'), (0, -1, 'W')],
    'S': [(0, 1, 'E'), (0, -1, 'W'), (1, 0, 'S')],
}


q = [pos]
visited = {}
finished = False

while len(q):
    if finished:
        break
    i = heappop(q)
    for dy, dx, dd in moves[i.d]:
        nx, ny = i.x + dx, i.y + dy
        if m[ny][nx] == '#':
            continue

        if m[ny][nx] == 'E':
            print(i.score + 1)
            finished = True
            break

        nscore = i.score + 1

        if i.d != dd:
            nscore += 1000

        if (ny, nx, dd) in visited and visited[(ny, nx, dd)] < nscore:
            continue
        visited[(ny, nx, dd)] = nscore
        heappush(q, Item(nscore, ny, nx, dd))
