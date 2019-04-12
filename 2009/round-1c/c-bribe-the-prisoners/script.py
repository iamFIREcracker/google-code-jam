def Bribe(a, b):
  if (a, b) in memo: return memo[(a, b)]

  r = 0
  for q in Q:
    if q >= a and q <= b:
      tmp = b - a + Bribe(a, q - 1) + Bribe(q + 1, b)
      if not r or tmp < r: r = tmp
  memo[(a, b)] = r
  return r

for case in xrange(input()):
  memo = {}
  (P, Q) = map(int, raw_input().split())
  Q = map(int, raw_input().split())
  print 'Case #%d: %d' % (case + 1, Bribe(1, P))
