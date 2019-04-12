for case in xrange(input()):
  mixtures = []
  for i in xrange(input()):
    needed = 1
    for i, ingredient in enumerate(raw_input().split()):
      if not i:
        name = ingredient
      elif ingredient.isupper():
        needed += 1
    mixtures.append((needed, name))
  
  bowls, empty = 0, 0
  done = []
  for needed, name in sorted(mixtures, reverse=True):
    empty -= needed
    if empty < 0:
      bowls += -empty
      empty = 0
    empty += needed - 1
    done.append(name)
    print done
  
  print 'Case #%d: %d' % (case + 1, bowls)
