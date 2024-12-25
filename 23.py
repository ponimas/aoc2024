#!/usr/bin/env python3
from collections import defaultdict
from itertools import combinations

# from pprint import pprint as print
from pyrsistent import pset

f = "test.23.txt"
f = "23.input.txt"

g = defaultdict(set)

for l in open(f):
    a, b = l.strip().split("-")
    g[a].add(b)
    g[b].add(a)

# part 1
components = set()


for c in g.keys():
    for a, b in combinations(g[c], 2):
        if b in g[a]:
            if "t" in {a[0], b[0], c[0]}:
                components.add(tuple(sorted([a, b, c])))

print(len(components))

# part 2
# https://www.youtube.com/watch?v=j_uQChgo72I


def bron_kerbosch(R, P, X):
    if not P and not X:
        cliques.append(R)
        return
    for v in P:
        bron_kerbosch(R.add(v), P & g[v], X & g[v])
        P = P.remove(v)
        X = X.add(v)


R = pset()
X = pset()
P = pset(g.keys())
cliques = []

bron_kerbosch(R, P, X)
cliques.sort(key=len)
print(",".join(sorted(list(cliques[-1]))))
