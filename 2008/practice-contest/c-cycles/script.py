def ReadInts():
  return list(map(int, raw_input().strip().split(' ')))

def Cross(a, b):
  for i in a:
    for j in b:
      yield (i, j)

def Neighbors(i, n):
  for j in xrange(1, n + 1):
    if j == i: continue
    if i in forbidden and j in forbidden[i]: continue
    yield j


for N in xrange(1, input() + 1):
  n, k = ReadInts()[0:2]

  forbidden = {}
  for _ in xrange(k):
    (s, d) = ReadInts()[0:2]
    if s in forbidden: forbidden[s].append(d)
    else: forbidden[s] = [d]

  for i in xrange(1, n + 1):

  break
