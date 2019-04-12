for case in xrange(1, input() + 1):
  N = input()
  r = []
  for i in xrange(N):
    n = -1
    for (j, c) in enumerate(raw_input()):
      if c == '1': n = j
    r.append(n)

  s = 0
  for i in xrange(N):
    if r[i] <= i: continue
    for j in xrange(i, N):
      if r[j] <= i: break
    for k in xrange(j, i, -1):
      tmp = r[k]
      r[k] = r[k - 1]
      r[k - 1] = tmp
      s += 1
  
  print "Case #%d: %d" % (case, s)
