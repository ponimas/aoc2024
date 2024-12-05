r, p = open('5.txt').read().split('\n\n')

rules = [tuple(l.split('|')) for l in r.split('\n')]
# rules.sort()
pages = [l.split(',') for l in p.strip().split('\n')]

s = 0
for pp in pages:
  for l, r in rules:
    if l in pp and r in pp:
      if pp.index(l) > pp.index(r):
        break
  else:
    i = len(pp) // 2
    s += int(pp[i])
print(s)


s = 0
for pp in pages:
  reordered = False
  while True:
    in_order = True
    for l, r in rules:
      if l in pp and r in pp:
        if pp.index(l) > pp.index(r):
          reordered = True
          in_order = False
          pp[pp.index(l)], pp[pp.index(r)] = pp[pp.index(r)], pp[pp.index(l)]
    if not reordered:
      break
    if reordered and in_order:
      i = len(pp) // 2
      s += int(pp[i])
      break
print(s)
