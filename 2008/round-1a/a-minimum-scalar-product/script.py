import operator
from itertools import *


for case in xrange(input()):
  n = input()
  v1 = sorted(map(int, raw_input().split()))
  v2 = sorted(map(int, raw_input().split()), reverse=True)
  print 'Case #%d: %d' % (case + 1,
                          sum(imap(operator.mul, v1, v2)))
