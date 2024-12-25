#! /usr/bin/env python3
from collections import Counter

data = open("1.txt").readlines()
a, b = list(), list()

for l in data:
    x, y = [int(i) for i in l.split()]
    a.append(x)
    b.append(y)

a.sort()
b.sort()

# part 1
print(sum(abs(x - y) for x, y in zip(a, b)))

# part 2
bb = Counter(b)

print(sum(x * bb[x] for x in a))
