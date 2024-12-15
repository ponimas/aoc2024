#!/usr/bin/env python3

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
