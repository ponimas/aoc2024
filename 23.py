#!/usr/bin/env python3
from collections import defaultdict, deque
from itertools import combinations

# from pprint import pprint as print
from pyrsistent import v

f = "test.23.txt"
f = "23.input.txt"

g = defaultdict(set)

for l in open(f):
    a, b = l.strip().split("-")
    g[a].add(b)
    g[b].add(a)

# print(g)

# part 1
components = set()


for c in g.keys():
    for a, b in combinations(g[c], 2):
        if b in g[a]:
            if "t" in {a[0], b[0], c[0]}:
                components.add(tuple(sorted([a, b, c])))

print(len(components))


R = set()
X = set()
P = list(g.keys())


# def bron_kerbosch(R, P, X):
#     if not P and not X:
#         print(R)  # Максимальная клика найдена
#         return
#     for v in P[:]:
#         bron_kerbosch(
#             R + [v], [u for u in P if u in neighbors[v]], [u for u in X if u in neighbors[v]]
#         )
#         P.remove(v)
#         X.append(v)


components = list()
for c in g.keys():
    q = deque()
    q.append(v(c))

    while len(q):
        p = q.popleft()
        l = p[-1]
        # print(p)
        for x in g[l]:
            for c in components:
                if len(c - {l, x}) == 0:
                    continue
            for enc in list(q):
                if len(set(enc) - {l, x}) == 0:
                    continue
            if x in p:
                continue

            if len(set(p) - g[x]) == 0:
                np = p.append(x)
                q.appendleft(np)
    print(p)
    components.append(set(p))
    print(tuple(sorted(p)))

print(sorted(components, key=len)[-1])
