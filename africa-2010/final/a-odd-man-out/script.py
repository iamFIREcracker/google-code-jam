for i in xrange(input()):
  input()
  memo = {}
  for n in raw_input().split():
    if n not in memo: memo[n] = 1
    else: del memo[n]
  print 'Case #%d: %s' % (i + 1, memo.keys()[0])
