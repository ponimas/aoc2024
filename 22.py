#!/usr/bin/env python3
from math import floor
from itertools import pairwise, islice
from collections import deque
from functools import cache
from heapq import heappush, nlargest
from line_profiler import profile

f = "test.22.txt"
f = "22.input.txt"


# https://docs.python.org/3/library/itertools.html#itertools-recipes
def sliding_window(iterable, n):
    "Collect data into overlapping fixed-length chunks or blocks."
    # sliding_window('ABCDEFG', 4) → ABCD BCDE CDEF DEFG
    iterator = iter(iterable)
    window = deque(islice(iterator, n - 1), maxlen=n)
    for x in iterator:
        window.append(x)
        yield tuple(window)


@cache
def transform(x):
    x ^= 64 * x
    x %= 16777216
    x ^= floor(x / 32)
    x %= 16777216
    x ^= 2048 * x
    x %= 16777216
    return x


@profile
def main():
    ll = open(f).read().strip().split("\n")
    s = 0
    prices = []

    # part 1
    for l in ll:
        n = int(l)
        p = [n % 10]
        for _ in range(2000):
            n = transform(n)
            p.append(n % 10)
        s += n
        prices.append(p)
    print(s)

    slopes = ([b - a for a, b in pairwise(p)] for p in prices)
    windows = []
    keys = set()

    for i, s in enumerate(slopes):
        ww = sliding_window(s, 4)
        window = {}

        for j, w in enumerate(ww):
            if w in window:
                continue
            keys.add(w)
            window[w] = prices[i][j + 4]
        windows.append(window)

    maximums = []

    for k in keys:
        w = [w.get(k, 0) for w in windows]
        s = sum(w)
        heappush(maximums, s)

    # 2174 is too low
    print(nlargest(1, maximums)[0])


if __name__ == "__main__":
    main()
