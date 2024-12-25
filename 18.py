#!/usr/bin/env python3
from collections import deque
from copy import copy

f = "test.txt"
sz = 6
bytes_n = 12

f = "18.txt"
sz = 70
bytes_n = 1024

start = (0, 0)
end = (sz, sz)

m = {(x, y): "." for x in range(sz + 1) for y in range(sz + 1)}

bytes = []
for l in open(f).readlines():
    (x, y) = l.split(",")
    bytes.append((int(x), int(y)))


deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]
q = deque([[start]])
visited = set()

# part 1
field = copy(m)
for b in bytes[:bytes_n]:
    field[b] = "#"

while len(q):
    p = q.popleft()
    x, y = p[-1]
    if (x, y) == end:
        # print(p)
        print(len(p) - 1)
        break
    for d in deltas:
        n = (x + d[0], y + d[1])
        if n not in field:
            continue
        if n in visited:
            continue
        if field[n] == "#":
            continue
        np = copy(p)
        np.append(n)
        visited.add(n)
        q.append(np)

# part 2
for i in range(1024, len(bytes)):
    visited = set()
    field = copy(m)
    q = deque([[start]])
    # print(bytes[:i])
    for b in bytes[:i]:
        field[b] = "#"
    found = False
    while len(q):
        p = q.popleft()
        x, y = p[-1]
        if (x, y) == end:
            found = True
            break
        for d in deltas:
            n = (x + d[0], y + d[1])
            if n not in field:
                continue
            if n in visited:
                continue
            if field[n] == "#":
                continue
            np = copy(p)
            np.append(n)
            visited.add(n)
            q.append(np)
    if not found:
        print(bytes[i - 1], i)
        break
