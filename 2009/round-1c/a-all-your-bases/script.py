for case in xrange(input()):
  s = raw_input()
  u = set(s)

  l = len(s)
  base = len(u)
  if base == 1:
    base += 1
  sum = 0
  values = {}
  for i, c in enumerate(s):
    if c not in values:
      if not values:
        values[c] = 1
      elif len(values) == 1:
        values[c] = 0
      else:
        values[c] = (len(values))%base
    sum += values[c]*base**(l - 1 - i)
  print 'Case #%d: %d' % (case + 1, sum)
