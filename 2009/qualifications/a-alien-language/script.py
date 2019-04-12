import re

L, D, N = map(int, raw_input().split())
words = [raw_input() for i in xrange(D)]
for case in xrange(N):
  reg = re.compile(raw_input().replace('(', '[').replace(')', ']'))
  matches = 0
  for w in words:
    if reg.match(w):
      matches += 1
  print 'Case #%d: %d' % (case + 1, matches)
