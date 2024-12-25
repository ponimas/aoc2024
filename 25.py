#!/usr/bin/env python3

f = "test.25.txt"
f = "25.input.txt"

keys = []
locks = []
for x in open(f).read().split("\n\n"):
    lns = x.strip().split("\n")
    y = [0, 0, 0, 0, 0]
    if lns[0] == "#" * 5:
        for l in lns[1:]:
            for i, p in enumerate(l):
                y[i] += p == "#"
        locks.append(y)
    else:
        for l in lns[:-1]:
            for i, p in enumerate(l):
                y[i] += p == "#"
        keys.append(y)


def fit(k, l):
    for a, b in zip(k, l):
        if a + b > 5:
            return False
    return True


i = 0
for lock in locks:
    for key in keys:
        if fit(key, lock):
            i += 1
print(i)
