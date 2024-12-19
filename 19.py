#!/usr/bin/env python3
from collections import deque

f = 'test.txt'
f = 'unsolved/19.input.txt'

towels, patterns = open(f).read().split('\n\n')

towels = [towel.strip() for towel in towels.split(',')]
patterns = patterns.strip().split('\n')

cnt = 0

for pattern in patterns:
    q = deque([pattern])
    while len(q):
        p = q.popleft()
        if p == '':
            cnt += 1
            break
        for t in towels:
            if p.startswith(t):
                q.appendleft(p[len(t) :])

print(cnt)  # 228

# part 2
towels = set(towels)


def find(pattern):
    ways = {}
    steps = [pattern[:i] for i in range(1, len(pattern) + 1)]

    for i, step in enumerate(steps):
        # print(step)
        step_counter = int(step in towels)
        for j in range(i - 1, -1, -1):
            d = step.removeprefix(steps[j])
            # print(step, steps[j], d)
            if d in towels:
                step_counter += ways[steps[j]]
        ways[step] = step_counter
    return ways[steps[-1]]


cnt = 0

for p in patterns:
    cnt += find(p)

print(cnt)  # 584553405070389
