NONE, NORTH, WEST, EAST, SOUTH = xrange(5)
LABELS = 'abcdefghijklmnopqrstuvwxyz'

for case in xrange(input()):
  h, w = map(int, raw_input().split())
  grid = [map(int, raw_input().split()) for i in xrange(h)]
  memo = {}
  for i in xrange(h):
    for j in xrange(w):
      memo[i, j] = [] 
  sinks = []
  for i in xrange(h):
    for j in xrange(w):
      values = []
      if i:
        values.append((grid[i - 1][j], NORTH))
      if j:
        values.append((grid[i][j - 1], WEST))
      if j != w - 1:
        values.append((grid[i][j + 1], EAST))
      if i != h - 1:  
        values.append((grid[i + 1][j], SOUTH))

      value = grid[i][j]
      direction = NONE
      for v, d in values:
        if v < value:
          value, direction = v, d
      
      if direction == NORTH:
        memo[i - 1, j] = [(i, j)] + memo[i - 1, j]
      elif direction == WEST:
        memo[i, j - 1] = [(i, j)] + memo[i, j - 1]
      elif direction == EAST:
        memo[i, j + 1] = [(i, j)] + memo[i, j + 1]
      elif direction == SOUTH:
        memo[i + 1, j] = [(i, j)] + memo[i + 1, j]
      else:
        sinks.append((i, j))

  paths = []
  for s in sinks:
    ls = [s] + memo[s]
    i = 0
    while i < len(ls):
      if len(memo[ls[i]]):
        ls = ls + memo[ls[i]]
      i += 1
    paths.append(ls)

  associations = {}
  output = ''
  for i in xrange(h):
    for j in xrange(w):
      for k, ls in enumerate(paths):
        if (i, j) in ls:
          if k not in associations:
            associations[k] = len(associations)
          output += LABELS[associations[k]]
      if j != w - 1:
        output += ' '
    if i != h - 1:
      output += '\n'
  print 'Case #%d:\n%s' % (case + 1, output)
