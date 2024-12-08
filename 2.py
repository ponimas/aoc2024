#! /usr/bin/env python3
import itertools

data = open('2.txt').readlines()

# part 1
cnt = 0
for l in data:
    ll = (int(x) for x in l.strip().split(' '))
    kk = [a - b for (a, b) in itertools.pairwise(ll)]
    cnt += all(1 <= x <= 3 for x in kk) or all(-3 <= x <= -1 for x in kk)
print(cnt)

# part 2
cnt = 0


class Break(Exception):
    pass


for l in data:
    ll = [int(x) for x in l.strip().split(' ')]
    kk = [a - b for (a, b) in itertools.pairwise(ll)]
    if all(1 <= x <= 3 for x in kk) or all(-3 <= x <= -1 for x in kk):
        cnt += 1
        continue
    try:
        for i in range(len(ll)):
            jj = ll[:i] + ll[i + 1 :]
            kk = [a - b for (a, b) in itertools.pairwise(jj)]
            if all(1 <= x <= 3 for x in kk) or all(-3 <= x <= -1 for x in kk):
                cnt += 1
                raise Break()
    except Break:
        pass


print(cnt)
