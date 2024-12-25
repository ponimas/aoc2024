#! /usr/bin/env python3
from operator import mul, add
from itertools import product

f = "test7.txt"
f = "7.txt"

cases = []
for l in open(f).readlines():
    t, v = l.split(":")
    vv = [int(x) for x in v.strip().split(" ")]
    cases.append([int(t), vv])

# part 1

s = 0
matched = set()
for i, [t, xx] in enumerate(cases):
    for ops in product([mul, add], repeat=len(xx) - 1):
        x, *tail = xx
        for y, op in zip(tail, ops):
            x = op(x, y)
            if x > t:
                break
        else:
            if x == t:
                matched.add(i)
                s += x
                break
print(s)


def con(a, b):
    return int(str(a) + str(b))


# part 2
for i, [t, xx] in enumerate(cases):
    if i in matched:
        continue
    for ops in product([con, mul, add], repeat=len(xx) - 1):
        x, *tail = xx
        for y, op in zip(tail, ops):
            x = op(x, y)
            if x > t:
                break
        else:
            if x == t:
                matched.add(i)
                s += x
                break
print(s)
