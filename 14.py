#!/usr/bin/env python3
import re
from copy import deepcopy

f = 'test.txt'
f = '14.txt'


rx = 'p=(?P<x>\d+),(?P<y>\d+) v=(?P<dx>-?\d+),(?P<dy>-?\d+)'
with open(f) as f:
    robots = [{k: int(v) for k, v in re.match(rx, l).groupdict().items()} for l in f if l != '']

field_sz = (11, 7)
field_sz = (101, 103)

# print(robots)
# robots =[{'x': 2, 'y': 4, 'dx':2, 'dy': -3}]

disp = [['.' for _ in range(field_sz[0])] for _ in range(field_sz[1])]


def move(i):
    dd = deepcopy(disp)
    found = False
    for robot in robots:
        nx = robot['x'] + robot['dx']
        if nx < 0:
            nx = field_sz[0] - abs(nx) % field_sz[0]
        if nx >= field_sz[0]:
            nx = abs(nx) % field_sz[0]
        ny = robot['y'] + robot['dy']
        if ny < 0:
            ny = field_sz[1] - abs(ny) % field_sz[1]
        if ny >= field_sz[1]:
            ny = abs(ny) % field_sz[1]
        robot['x'] = nx
        robot['y'] = ny

        dd[ny][nx] = '*'

    for y in range(field_sz[1]):
        l = ''.join(dd[y])
        if '**********' in l:
            found = True

    if found:
        print('\n'.join(''.join(l) for l in dd))
        print(i)


for i in range(10000):
    move(i)

# q = defaultdict(int)

# rr = Counter((r['x'], r['y']) for r in robots)
# for (x, y), c in rr.items():
#     if x < field_sz[0] // 2:
#         a = 'L'
#     elif x > field_sz[0] // 2:
#         a = 'R'
#     else:
#         continue
#     if y < field_sz[1] // 2:
#         b = 'U'
#     elif y > field_sz[1] // 2:
#         b = 'D'
#     else:
#         continue
#     q[a + b] += c

# m = 1
# for x in q.values():
#     m *= x

# print(m)
