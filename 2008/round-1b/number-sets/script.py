""" We need only factors greater than the prompted prime, and smaller than the
size of the interval
"""
def factor(n, start, stop):
  if 1 >= start:
    yield 1
  if 1 > stop:
    return
  i = 2
  limit = n**.5
  while i <= limit:
    if not n%i:
      if i >= start:
        yield i
      if i > stop:
        return
      n /= i
      limit = n**.5
    else:
      i += 1
  if n > 1:
    if n >= start:
      yield n

for case in xrange(input()):
  start, stop, prime = map(int, raw_input().split())

  primes = [p for p in prime1
  numbers = []
  links = []
  factors = []
  i = start
  while i < stop + 1:
    numbers.append(i)

    links.append(i - start)
    factors.append([f for f in factor(i, prime, stop - start)])
    i += 1
  
  l = len(numbers)
  for i in xrange(l):
    for j in xrange(i + 1, l):
      if links[i] == links[j]:
        continue
      for f in factors[i]:
        if f in factors[j] and f >= prime:
          for k in xrange(l):
            if links[k] == links[j]:
              links[k] = links[i]
          links[j] = links[i]

  print 'Case #%d: %d' % (case + 1, len(set(links)))
