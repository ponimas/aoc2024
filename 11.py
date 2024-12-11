#!/usr/bin/env python3
from collections import defaultdict

f = 'test.txt'
f = '11.txt'

stones = open(f).readline().strip().split(' ')
# print(stones)

cache_map = defaultdict(lambda: defaultdict(lambda: None))
cache = dict()


def cal(s, steps):
    cached = cache.get((s, steps))
    if cached is not None:
        return cached

    v = cache_map[s]
    if isinstance(v, tuple):
        cache[(s, steps)] = 2 if steps == 1 else cal(v[0], steps - 1) + cal(v[1], steps - 1)

        return cache[(s, steps)]
    elif isinstance(v, str):
        cache[(s, steps)] = 1 if steps == 1 else cal(v, steps - 1)
        return cache[(s, steps)]
    else:
        if s == '0':
            cache_map[s] = '1'
        elif len(s) % 2 == 0:
            mid = len(s) // 2
            cache_map[s] = (s[:mid], s[mid:].lstrip('0') or '0')
        else:
            cache_map[s] = str(int(s) * 2024)

        return cal(s, steps)


print(sum(cal(i, 75) for i in stones))
