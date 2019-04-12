for case in xrange(input()):
  P, K, L = map(int, raw_input().split())
  freqs = map(int, raw_input().split())

  keys = [[] for i in xrange(K)]
  index = 0
  keypress = 0
  for freq in reversed(sorted(freqs)):
    while len(keys[index]) >= P:
      index = (index + 1)%len(keys)
    keys[index].append(freq)

    keypress += len(keys[index])*freq
    index = (index + 1)%len(keys)
  print 'Case #%d: %d' % (case + 1, keypress)
