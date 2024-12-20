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

# for machine in machines:
#     xa, ya = (machine['xa'], machine['ya'])
#     xb, yb = (machine['xb'], machine['yb'])
#     xp, yp = (machine['xp'] + 10000000000000, machine['yp'] + 10000000000000)

#     j = min(yp // ya, xp // xa)
#     k = 0
#     while True:
#         x = xa * j + xb * k
#         y = ya * j + yb * k
#         if x == xp and y == yp:
#             print("found", j, k)
#             break
#         j -= 1
#         # print("XXX", xp - xa * j + xb * k)
#         # print("YYY", yp - ya * j + yb * k)

#         while xa * j + xb * k < xp and ya * j + yb * k < yp:
#             k += 1

#         print(j, k)


"""
одна из кнопок ведёт больше по y, другая по x
мне нужно нажать вторую кнопку минимальное количество раз
можно найти
"""


print('====')
xp = 10000000012748
yp = 10000000012176

xa = 26
xb = 67

ya = 66
yb = 21

xx = xa + xb
yy = ya + yb

d = xp

j = 0
c = 0

while True:
    if d % xx == 0:
        j = d // xx
        # print(xx, yy, j)
        # print("XXX", j * xx, xa * c, j * xx + xa * c, xp)
        # print("YYY", j * yy, ya * c, j * yy + ya * c, yp, yp - (j * yy + ya * c))

        if j * yy + yb * c == yp:
            break

    d -= xb
    c += 1

# print(d)

print('----', j * xx, xa * c, j * xx + xa * c, xp)
print('----', j * yy, ya * c, j * yy + ya * c, yp)
print(j)
print(c)

print(yp - yy * j)

if (yp - yy * j) % ya == 0:
    print('yes')
