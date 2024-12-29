#!/usr/bin/env python3
f = "test.9.txt"
f = "9.txt"

m = []
last_block = 0
for i, x in enumerate(open(f).readline().strip()):
    sz = int(x)
    m += ["." if i % 2 else i // 2] * sz
    if i % 2 == 0:
        last_block = i // 2


def checksum(mm):
    s = 0
    for i, x in enumerate(mm):
        if x != ".":
            s += i * int(x)
            # print(i, int(x), i * int(x), s)
    print(s)


mm = m[:]
l = 0

r = len(mm) - 1

while True:
    if l == r:
        break
    if mm[r] == ".":
        r -= 1
        continue
    if mm[l] == ".":
        mm[l], mm[r] = mm[r], mm[l]
    l += 1

checksum(mm)

mm = m[:]


def find_space(start_pos=0):
    while True:
        if mm[start_pos] != ".":
            start_pos += 1
        else:
            break
    end_pos = start_pos
    while end_pos < len(mm) - 1:
        if mm[end_pos + 1] == ".":
            end_pos += 1
        else:
            break
    return start_pos, end_pos


def find_block(block_id, end_pos):
    while True:
        if mm[end_pos] != block_id:
            end_pos -= 1
        else:
            break
    start_pos = end_pos
    while True:
        if mm[start_pos - 1] == block_id:
            start_pos -= 1
        else:
            break
    return start_pos, end_pos


b = len(mm) - 1

# suboptial solution, but it works
for block_id in range(last_block, 0, -1):
    ba, bb = find_block(block_id, b)
    skip = False
    free_start = 0
    while True:
        aa, ab = find_space(free_start)
        if ab >= ba:
            skip = True
            break
        if ab - aa < bb - ba:
            free_start = ab + 1
            continue
        break
    if skip:
        b = aa
        continue

    mm[aa : aa + (bb - ba) + 1] = mm[ba : bb + 1]
    mm[ba : bb + 1] = ["."] * (bb - ba + 1)
    # print("".join(map(str, mm)))
    b = ba - 1

checksum(mm)
