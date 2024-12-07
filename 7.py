from operator import mul, add
from functools import reduce
from itertools import product

f = 'test7.txt'
f = '7.txt'

cases = []
for l in open(f).readlines():
    t, v = l.split(':')
    vv = [int(x) for x in v.strip().split(' ')]
    cases.append([int(t), vv])

# part 1

s = 0
for t, xx in cases:
    for ops in product([mul, add], repeat=len(xx) - 1):
        x, *tail = xx
        for y, op in zip(tail, ops):
            x = op(x, y)
            if x > t:
                break
        else:
            if x == t:
                s += x
                break
print(s)
