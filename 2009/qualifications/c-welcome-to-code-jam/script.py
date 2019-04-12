PATTERN = 'welcome to code jam'

for case in xrange(input()):
  text = raw_input()
  subset = {}
  for i in xrange(1, len(PATTERN) + 1):
    subset[PATTERN[:i]] = 0
  for c in text:
    if c in PATTERN:
      for key in subset.keys():
        if c == key:
          subset[c] += 1
        if key + c in subset:
          if subset[key]:
            subset[key + c] += subset[key]
  print 'Case #%d: %04d' % (case + 1, subset[PATTERN]%10000)
