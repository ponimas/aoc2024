#!/usr/bin/env python3
import re
from collections import namedtuple

rx = "Register A: (?P<A>\d+)\nRegister B: (?P<B>\d+)\nRegister C: (?P<C>\d+)\n\nProgram: (?P<programm>(\d,?)+)\n"

state = namedtuple("state", ["a", "b", "c", "pos", "out"])

f = "test.txt"
f = "17.txt"

data = re.match(rx, open(f).read()).groupdict()
initstate = state(int(data["A"]), int(data["B"]), int(data["C"]), 0, [])

programm = [int(x) for x in data["programm"].split(",")]


def combo(x, state):
    if x <= 3:
        return x
    if x == 4:
        return state.a
    if x == 5:
        return state.b
    if x == 6:
        return state.c
    return -1


def step(s):
    op = programm[s.pos]
    x = programm[s.pos + 1]
    cx = combo(x, s)

    if op == 0:
        return state(s.a // (2**cx), s.b, s.c, s.pos + 2, s.out)
    if op == 1:
        return state(s.a, s.b ^ x, s.c, s.pos + 2, s.out)
    if op == 2:
        return state(s.a, cx % 8, s.c, s.pos + 2, s.out)
    if op == 3:
        if s.a == 0:
            return state(s.a, s.b, s.c, s.pos + 2, s.out)
        return state(s.a, s.b, s.c, x, s.out)
    if op == 4:
        return state(s.a, s.b ^ s.c, s.c, s.pos + 2, s.out)
    if op == 5:
        s.out.append(cx % 8)
        return state(s.a, s.b, s.c, s.pos + 2, s.out)
    if op == 6:
        return state(s.a, s.a // (2**cx), s.c, s.pos + 2, s.out)
    if op == 7:
        return state(s.a, s.b, s.a // (2**cx), s.pos + 2, s.out)


s = initstate
while True:
    s = step(s)
    if s.pos >= len(programm):
        break

dt = 2 ** ((len(programm) - 1) * 3)
p = len(programm) - 1
i = dt
xx = [None]

while True:
    s = state(i, 0, 0, 0, [])
    while True:
        s = step(s)
        if s.pos >= len(programm):
            break

    if s.out == programm:
        print(i, s.out)
        break
    found = False
    if programm[p:] == s.out[p:]:
        print("more", dt, p, i)
        print(s.out)
        p -= 1
        dt = dt // 32 or 1

    # print(p, i, dt, programm, s.out)
    i += dt

    if s.out == programm:
        print(s.out)
        print(i)
        break
