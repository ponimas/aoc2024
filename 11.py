#!/usr/bin/env python3
from collections import deque

f = 'test.txt'
# f = "11.txt"

stones = open(f).readline().strip().split(' ')
# print(stones)


q = deque(stones)


def transform(stones):
    for _ in range(len(q)):
        stone = q.popleft()
        if stone == '0':
            q.append('1')
        elif len(stone) % 2 == 0:
            mid = len(stone) // 2
            l = stone[:mid]
            r = stone[mid:].lstrip('0') or '0'

            q.append(l)
            q.append(r)
        else:
            q.append(str(int(stone) * 2024))


for i in range(25):
    transform(stones)

# print(q)
print(len(q))
