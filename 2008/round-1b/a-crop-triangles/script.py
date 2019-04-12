import itertools

def factorial(n):
  if n == 0: return 1
  if n not in memo:
    memo[n] = n*factorial(n - 1)
  return memo[n]

#--------------------------------------------------
# def factorial(n):
#   s = 1
#   while n:
#     s *= n
#     n -= 1
#   return s
#-------------------------------------------------- 

def multinomial(iterable):
  s = 0
  den = 1
  for i in iterable:
    den *= factorial(i)
    s += i
  return factorial(s)/den

trees = [(i, j) for i in xrange(3) for j in xrange(3)]
ok = []
for (t1, t2, t3) in itertools.combinations(trees, 3):
  if (t1[0] + t2[0] + t3[0])%3 == 0 and (t1[1] + t2[1] + t3[1])%3 == 0:
    ok.append((t1, t2, t3))

memo = {}
for case in xrange(input()):
  n, A, B, C, D, x, y, M = map(int, raw_input().split())

  trees = [[0 for _ in xrange(3)] for _ in xrange(3)]
  X, Y = x, y
  trees[X%3][Y%3] += 1
  for i in xrange(1, n):
    X, Y = (A*X + B)%M, (C*Y + D)%M
    trees[X%3][Y%3] += 1

  crop = 0
  for ((i1, j1), (i2, j2), (i3, j3)) in ok:
    crop += multinomial([trees[i1][j1], trees[i2][j2], trees[i3][j3]])

  print 'Case #%d: %s' % (case + 1, crop)
