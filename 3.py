#! /usr/bin/env python3
import re

data = open("test.txt").read()

# Part 1
rx = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
print(sum(int(x) * int(y) for (x, y) in rx.findall(data)))

# Part 2

rx = re.compile(r"(mul\((?P<a>\d{1,3}),(?P<b>\d{1,3})\))|(?P<do>do\(\))|(?P<dont>don\'t\(\))")

state = "do"
sum = 0
for r in rx.finditer(data):
    if r.groupdict()["do"]:
        state = "do"
        continue
    if r.groupdict()["dont"]:
        state = "dont"
    if state == "dont":
        continue
    sum += int(r.groupdict()["a"]) * int(r.groupdict()["b"])
print(sum)
