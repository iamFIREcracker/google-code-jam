def ReadInts():
  return list(map(int, raw_input().strip().split(' ')))

for N in xrange(1, input() + 1):
  W, B = ReadInts()

  if B%2: print 'Case #%d: BLACK' % N
  else: print 'Case #%d: WHITE' % N
