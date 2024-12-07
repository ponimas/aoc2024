from collections import defaultdict, namedtuple
from bisect import bisect_right, bisect_left

f = 'test.txt'

mx = defaultdict(list)
my = defaultdict(list)
point = namedtuple('point', ['x', 'y'])

r = open(f).readlines()
sz = (len(r[0].strip()) - 1, len(r) - 1)

for y, l in enumerate(r):
    for x, p in enumerate(l.strip()):
        if p != '.':
            if p != '#':
                pos = point(x, y)
                g = p
            else:
                mx[x].append(y)
                my[y].append(x)

dist = set([pos])
dist_t = set([(pos, g)])
stop = False
c = 0

while True:
    if g == '^':
        b = bisect_left(mx[pos.x], pos.y)
        if b == 0:
            ny = 0
            stop = True
        else:
            ny = mx[pos.x][b - 1] + 1
        # print("next is", pos.x, ny, ">")
        for y in range(ny, pos.y):
            np = point(pos.x, y)
            if np in dist:
                c += 1
                print(np)
            # print()
            dist.add(np)
        if stop:
            break
        pos = point(pos.x, ny)
        g = '>'
        continue

    elif g == 'v':
        b = bisect_right(mx[pos.x], pos.y)
        if b == len(mx[pos.x]):
            ny = sz[1]
            stop = True
        else:
            ny = mx[pos.x][b] - 1
        # print("next is", pos.x, ny, "<")
        for y in range(pos.y, ny + 1):
            np = point(pos.x, y)
            if np in dist:
                c += 1
                print(np)
            # print(point(pos.x, y))
            dist.add(np)
        if stop:
            break
        pos = point(pos.x, ny)
        g = '<'
        continue

    elif g == '>':
        b = bisect_right(my[pos.y], pos.x)
        if b == len(my[pos.y]):
            nx = sz[0]
            stop = True
        else:
            nx = my[pos.y][b] - 1
        # print("next is", nx, pos.y, "v")
        for x in range(pos.x, nx + 1):
            np = point(x, pos.y)
            if np in dist:
                c += 1
                print(np)
            dist.add(np)
        if stop:
            break
        pos = point(nx, pos.y)
        g = 'v'
        continue
    elif g == '<':
        b = bisect_left(my[pos.y], pos.x)
        if b == 0:
            nx = 0
            stop = True
        else:
            nx = my[pos.y][b - 1] + 1
        # print("next is", nx, pos.y, "^")
        for x in range(nx, pos.x):
            np = point(x, pos.y)
            if np in dist:
                c += 1
                print(np)
            # print(point(x, pos.y))
            dist.add(np)
        if stop:
            break
        pos = point(nx, pos.y)
        g = '^'
        continue

print(len(dist))
print(c)
