#!/usr/bin/env python3
import re
from collections import namedtuple, deque

f = "test.24.txt"
f = "24.input.txt"

v, gg = open(f).read().split("\n\n")

vals = {}
for v in v.split("\n"):
    g, i = v.split(": ")
    vals[g] = bool(int(i))


c = namedtuple("c", ["l", "op", "r", "d"])

rx = r"(?P<l>\w+) (?P<op>\w+) (?P<r>\w+) -> (?P<d>\w+)"
ops = deque(c(**re.match(rx, l).groupdict()) for l in gg.strip().split("\n"))

while len(ops):
    op = ops.popleft()
    if op.l not in vals or op.r not in vals:
        ops.append(op)
        continue
    match op.op:
        case "AND":
            a = lambda x, y: x and y
        case "OR":
            a = lambda x, y: x or y
        case "XOR":
            a = lambda x, y: x ^ y
    vals[op.d] = a(vals[op.l], vals[op.r])

ans = []
for k, v in vals.items():
    if k.startswith("z"):
        ans.append((k, v))
ans.sort(key=lambda x: x[0], reverse=True)
i = 0

for p, x in ans:
    print(p, int(x))
    i = (i << 1) | int(x)

print(i)
