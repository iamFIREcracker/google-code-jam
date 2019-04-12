from math import hypot
from copy import deepcopy

import pylab

def ReadInts():
  return list(map(int, fd_in.readline().strip().split(' ')))

def Cross(a, b):
  for i in a:
    for j in b:
      yield (i, j)

def ClusterDistance(c1, c2):
  max_d = None
  for (p1, p2) in Cross(c1, c2):
    d = hypot(p2[0] - p1[0], p2[1] - p1[1])
    if not max_d or d > max_d: max_d = d

  return max_d

def DistanceMatrix(clusters):
  matrix = []
  for i in xrange(len(clusters)):
    matrix.append([])
    for j in xrange(len(clusters)):
      if i == j: matrix[i].append(0)
      else:
        matrix[i].append(ClusterDistance(clusters[i], clusters[j]))

  return matrix

def ClosestClusters(clusters):
  min_d = None
  matrix = DistanceMatrix(clusters)
  for i in xrange(len(matrix)):
    for j in xrange(i + 1, len(matrix)):
      d = matrix[i][j]
      if min_d is None or d <= min_d:
        if d == min_d:
          closest.append((i, j))
        else:
          closest = [(i, j)]
        min_d = d
  return closest

def ClusterSize(c):
  for (i, (x, y)) in enumerate(c):
    if i == 0: (mx, my, Mx, My) = (x, y, x, y)
    else:
      if x < mx: mx = x
      elif x > Mx: Mx = x
      if y < my: my = y
      elif y > My: My = y
  return (Mx - mx, My - my)

def aggregate(clusters, k):
  if len(clusters) == k:
    max_d = None
    for c in clusters:
      d = max(ClusterSize(c))
      if max_d is None or d > max_d: max_d = d
    return max_d

  min_d = None
  for (i, j) in ClosestClusters(clusters):
    old = deepcopy(clusters)
    clusters[i] += clusters[j]
    clusters.pop(j)
    d = aggregate(clusters, k)
    if min_d is None or d < min_d: min_d = d
    clusters = old
  return min_d  

fd_in = open('B-large-practice.in')
fd_in = open('test')
fd_out = open('out', 'w')
for N in xrange(1, int(fd_in.readline()) + 1):
  n, k = ReadInts()[0:2]

  points = [tuple(ReadInts()[0:2]) for _ in xrange(n)]
  clusters = [[t] for t in points]

  max_d = aggregate(clusters, k)

  print k
  print clusters

  x = map(lambda (x, y): x, points)
  y = map(lambda (x, y): y, points)
  pylab.plot(x, y, 'o')

  pylab.grid(True)
  pylab.show()

  print 'Case #%d: %d' % (N, max_d)
  fd_out.write('Case #%d: %d\n' % (N, max_d))
