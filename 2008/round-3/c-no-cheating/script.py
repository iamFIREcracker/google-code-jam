for case in xrange(input()):
  row, col = map(int, raw_input().split())
  even, odd = 0, 0
  for i in xrange(row):
    places = map(int, raw_input().replace('.', '1').replace('x', '0'))
    even += sum(places[::+2])
    odd  += sum(places[1::+2])
  print 'Case #%d: %s' % (case + 1, max(even, odd))
    
