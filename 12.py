#!/usr/bin/env python3
from collections import deque

f = "test.txt"
f = "12.txt"

with open(f) as fl:
    m = [l.strip() for l in fl]
visited = [[False for _ in l] for l in m]

# print(m)
# print(visited)

p = (0, 0)

deltas = [(-1, 0, "U"), (1, 0, "D"), (0, -1, "L"), (0, 1, "R")]

positions = deque((y, x) for y in range(len(m)) for x in range(len(m[0])))
connected = []


def count_wallls(d, pp):
    c = 0
    while len(pp):
        p = pp.pop()
        c += 1
        while True:
            if d in {"U", "D"}:
                l = (p[0], p[1] - 1)
                r = (p[0], p[1] + 1)
                if l in pp:
                    p = l
                    pp.remove(l)
                    continue
                if r in pp:
                    p = r
                    pp.remove(r)
                    continue
                break
            else:
                u = (p[0] - 1, p[1])
                d = (p[0] + 1, p[1])
                if u in pp:
                    p = u
                    pp.remove(u)
                    continue
                if d in pp:
                    p = d
                    pp.remove(d)
                    continue
                break
    return c


total = 0
total2 = 0
for p in positions:
    if visited[p[0]][p[1]]:
        continue

    v = m[p[0]][p[1]]

    q = deque([p])
    component = set([p])
    perimeter = 0

    walls = {"U": [], "D": [], "L": [], "R": []}

    while len(q):
        (y, x) = q.popleft()
        if visited[y][x]:
            continue
        visited[y][x] = True

        for dy, dx, d in deltas:
            ny = y + dy
            nx = x + dx

            if 0 <= nx < len(m[0]) and 0 <= ny < len(m):
                if m[ny][nx] == v:
                    if not visited[ny][nx]:
                        component.add((ny, nx))
                        q.append((ny, nx))
                    continue

            perimeter += 1
            walls[d].append((y, x))

    total2 += len(component) * sum(count_wallls(d, walls[d]) for d in "UDRL")
    total += len(component) * perimeter

print(total)
print(total2)
