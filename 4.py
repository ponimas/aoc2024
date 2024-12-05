import itertools
from pprint import pprint

data = open('4.txt').readlines()

grid = {}
for y, l in enumerate(data):
  for x, s in enumerate(l):
    grid[(x, y)] = s


# part 1
def nxt(x, y, dx, dy):
  return x + dx, y + dy


directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]

result = 0
for y in range(len(data)):
  for x in range(len(data[0])):
    if grid.get((x, y)) != 'X':
      continue
    for dx, dy in directions:
      nx, ny = nxt(x, y, dx, dy)
      if grid.get((nx, ny)) == 'M':
        nx, ny = nxt(nx, ny, dx, dy)
        if grid.get((nx, ny)) == 'A':
          nx, ny = nxt(nx, ny, dx, dy)
          if grid.get((nx, ny)) == 'S':
            result += 1

print(result)

result = 0
for y in range(len(data)):
  for x in range(len(data[0])):
    if grid.get((x + 1, y + 1)) != 'A':
      continue

    result += (
      (
        grid.get((x, y)) == 'M'
        and grid.get((x + 2, y)) == 'M'
        and grid.get((x, y + 2)) == 'S'
        and grid.get((x + 2, y + 2)) == 'S'
      )
      or (
        grid.get((x, y)) == 'M'
        and grid.get((x + 2, y)) == 'S'
        and grid.get((x, y + 2)) == 'M'
        and grid.get((x + 2, y + 2)) == 'S'
      )
      or (
        grid.get((x, y)) == 'S'
        and grid.get((x + 2, y)) == 'S'
        and grid.get((x, y + 2)) == 'M'
        and grid.get((x + 2, y + 2)) == 'M'
      )
      or (
        grid.get((x, y)) == 'S'
        and grid.get((x + 2, y)) == 'M'
        and grid.get((x, y + 2)) == 'S'
        and grid.get((x + 2, y + 2)) == 'M'
      )
    )
    # print(x, y, result)

print(result)
