from decimal import *

setcontext(Context(prec=1000))
d = Decimal(3) + Decimal(5).sqrt()

for case in xrange(input()):
  n = Decimal(raw_input())
  print 'Case #%d: %03d' % (case + 1, d**n) 
