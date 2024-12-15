#!/usr/bin/env python3

from collections import deque

f = 'test.txt'
# f = "15.txt"

a, b = open(f).read().split('\n\n')

w = [list(l) for l in a.split('\n')]

found = False
for y, l in enumerate(w):
    if found:
        break
    for x, p in enumerate(l):
        if p == '@':
            pos = (y, x)
            found = True
            break

moves = b.replace('\n', '')
deltas = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}


def prn(w):
    a = '\n'.join(''.join(l) for l in w)
    print(a)


def move(p, move):
    d = deltas[move]
    np = p

    while True:
        np = (np[0] + d[0], np[1] + d[1])

        if w[np[0]][np[1]] == '#':
            return p
        if w[np[0]][np[1]] == '.':
            break

    while np != p:
        i = (np[0] - d[0], np[1] - d[1])
        w[np[0]][np[1]], w[i[0]][i[1]] = w[i[0]][i[1]], w[np[0]][np[1]]
        np = i

    return p[0] + d[0], p[1] + d[1]


for m in moves:
    pos = move(pos, m)

s = 0
for y, l in enumerate(w):
    for x, p in enumerate(l):
        if p == 'O':
            s += 100 * y + x
print(s)
ww = []
for y, l in enumerate(a.split('\n')):
    ll = []
    for p in l:
        if p in '#.':
            ll.append(p)
            ll.append(p)
        elif p == 'O':
            ll.append('[')
            ll.append(']')
        else:
            ll.append(p)
            ll.append('.')
    if '@' in ll:
        pos = (y, ll.index('@'))
    ww.append(ll)

# prn(ww)


def move2(p, m):
    if m == '<':
        nx = p[1]
        while True:
            nx -= 1
            j = ww[p[0]][nx]
            if j == '#':
                return p
            if j == '.':
                break
        ww[p[0]][nx : p[1]] = ww[p[0]][nx + 1 : p[1] + 1]
        ww[p[0]][p[1]] = '.'
        return (p[0], p[1] - 1)

    if m == '>':
        nx = p[1]
        while True:
            nx += 1
            j = ww[p[0]][nx]
            if j == '#':
                return p
            if j == '.':
                break
        ww[p[0]][p[1] : nx] = ww[p[0]][p[1] - 1 : nx - 1]
        ww[p[0]][p[1]] = '.'
        return (p[0], p[1] + 1)
    if m == '^':
        if ww[p[0] - 1][p[1]] == '[':
            b = (p[0] - 1, p[1])
        elif ww[p[0] - 1][p[1]] == ']':
            b = (p[0] - 1, p[1] - 1)
        elif ww[p[0] - 1][p[1]] == '#':
            return p
        else:
            ww[p[0] - 1][p[1]], ww[p[0]][p[1]] = '@', '.'
            return (p[0] - 1, p[1])

        affected = {b}
        q = deque([b])

        while len(q) > 0:
            (by, bx) = q.popleft()

            if ww[by - 1][bx] == '.' and ww[by - 1][bx + 1] == '.':
                continue

            if ww[by - 1][bx] == '#' or ww[by - 1][bx + 1] == '#':
                # block
                return p

            if ww[by - 1][bx] == ']':
                nn = (by - 1, bx - 1)
                if nn in affected:
                    continue
                affected.add(nn)
                q.appendleft(nn)
            if ww[by - 1][bx + 1] == '[':
                nn = (by - 1, bx + 1)
                if nn in affected:
                    continue
                affected.add(nn)
                q.appendleft(nn)
            if ww[by - 1][bx] == '[':
                nn = (by - 1, bx)
                if nn in affected:
                    continue
                affected.add(nn)
                q.appendleft(nn)
        a = list(affected)
        a.sort()
        for y, x in a:
            ww[y - 1][x], ww[y - 1][x + 1], ww[y][x], ww[y][x + 1] = (
                ww[y][x],
                ww[y][x + 1],
                ww[y - 1][x],
                ww[y - 1][x + 1],
            )
        ww[p[0]][p[1]], ww[p[0] - 1][p[1]] = ww[p[0] - 1][p[1]], ww[p[0]][p[1]]
    if m == 'v':
        if ww[p[0] + 1][p[1]] == '[':
            b = (p[0] + 1, p[1])
        elif ww[p[0] + 1][p[1]] == ']':
            b = (p[0] + 1, p[1] - 1)
        elif ww[p[0] + 1][p[1]] == '#':
            return p
        else:
            ww[p[0] + 1][p[1]], ww[p[0]][p[1]] = '@', '.'
            return (p[0] + 1, p[1])
    return p


for m in moves[:6]:
    prn(ww)
    pos = move2(pos, m)
    prn(ww)
