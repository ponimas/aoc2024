#!/usr/bin/env python3
from collections import deque

f = 'test.txt'
f = '12.txt'

with open(f) as fl:
    m = [l.strip() for l in fl]
visited = [[False for _ in l] for l in m]

# print(m)
# print(visited)

p = (0, 0)

deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]

positions = deque((y, x) for y in range(len(m)) for x in range(len(m[0])))
connected = []


total = 0
for p in positions:
    if visited[p[0]][p[1]]:
        continue

    v = m[p[0]][p[1]]

    q = deque([p])
    component = set([p])
    perimeter = 0

    while len(q):
        # print("---", v, component, perimeter)
        (y, x) = q.popleft()
        if visited[y][x]:
            continue
        visited[y][x] = True
        # if v == 'B':
        #     print('aaaaa')

        for dy, dx in deltas:
            ny = y + dy
            nx = x + dx

            if 0 <= nx < len(m[0]) and 0 <= ny < len(m):
                if m[ny][nx] == v:
                    if not visited[ny][nx]:
                        component.add((ny, nx))
                        q.append((ny, nx))
                else:
                    perimeter += 1
            else:
                perimeter += 1
            # if v == 'B':
            #     print((x, y), (nx, ny), m[ny][nx], perimeter)

        # print((x, y), perimeter)
    print('---', v, len(component), perimeter)
    total += len(component) * perimeter

print(total)
