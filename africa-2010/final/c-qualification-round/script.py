import sys

for i in xrange(input()):
  values = map(int, raw_input().split())
  N = values.pop(0)
  C = values.pop(0)
  w = 0
  while any(values):
    values.sort(reverse=True)
    if C != N and values[C] != 0:
      d = values[C - 1] - values[C] + 1
    else:
      d = values[C - 1]
    j = 0
    while j < C:
      if values[j] == 0: break
      values[j] -= d
      j += 1
    if j == C:
      w += d
    else:
      break
  print 'Case #%d: %d' % (i + 1, w)
