from math import hypot
from itertools import combinations

def ReadInts():
  return list(map(int, raw_input().strip().split(' ')))

def Distance(p1, p2):
  return hypot(p2[0] - p1[0], p2[1] - p1[1])

for N in xrange(1, input() + 1):
  n, k = ReadInts()[0:2]

  points = [ReadInts()[0:2] for _ in xrange(n)]

  print 'Case #%d: %d' % (N, -1)





