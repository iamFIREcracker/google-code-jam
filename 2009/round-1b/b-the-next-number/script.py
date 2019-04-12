def next_permutation(s):
  for i in reversed(xrange(len(s))):
    if s[i] > s[i-1]:
      break
  else:
    return []

  k = i
  for j in xrange(i, len(s)):
    if s[k] >= s[j] and s[j] > s[i-1]:
      k = j
  t = s[i-1]
  s[i-1] = s[k]
  s[k] = t
  s[i:] = s[len(s)-1:i-1:-1]
  return s

for case in xrange(input()):
  digits = '0' + raw_input()
  s = next_permutation(list(digits))
  if s[0] == '0': s.pop(0)
  print 'Case #%d: %s' % (case + 1, ''.join(s))
