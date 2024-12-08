from collections import defaultdict, namedtuple

f = 'test.txt'
# f = '6.txt'

none = lambda: None
lab = defaultdict(lambda: defaultdict(none))

point = namedtuple('point', ['x', 'y'])

r = open(f).readlines()
sz = (len(r[0].strip()) - 1, len(r) - 1)

for y, l in enumerate(r):
    for x, p in enumerate(l.strip()):
        if p == '#':
            lab[x][y] = '#'
            continue
        if p != '.':
            pos = point(x, y)
            g = p
        lab[x][y] = '.'

# pprint(lab)

deltas = {'>': (1, 0), '<': (-1, 0), '^': (0, -1), 'v': (0, 1)}
turns = {'>': 'v', '<': '^', '^': '>', 'v': '<'}

visited = set()

p = pos
d = g

while True:
    delta = deltas[d]
    nx = p.x + delta[0]
    ny = p.y + delta[1]
    nxt = lab[nx][ny]

    if nxt == '#':
        d = turns[d]
        # print("turn", d)
    elif nxt is None:
        break
    else:
        # print(p)
        p = point(nx, ny)
        visited.add(p)

print(len(visited))

p = pos
d = g

c = 0
while True:
    lab[p.x][p.y] = d

    delta = deltas[d]
    nx = p.x + delta[0]
    ny = p.y + delta[1]
    nxt = lab[nx][ny]

    if nxt == '#':
        d = turns[d]
        print('turn', d, p)
        continue

    if nxt is None:
        break
    # print(nxt)
    if nxt == turns[d]:
        print(nxt, p)
        c += 1
    p = point(nx, ny)
    visited.add(p)

print(c)
