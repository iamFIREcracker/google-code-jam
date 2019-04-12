def ReadInts():
  return list(map(int, raw_input().strip().split(' ')))

def IsHappy(n, b):
  hystory = [n]
  for i in xrange(b**3):
    if (b, n) in memo: return memo[(b, n)]
    sum = 0
    while n:
      n, d = divmod(n, b)
      sum += d**2
    n = sum
    if n in hystory:
      found = False
      break
    if n == 1: 
      found = True
      break
    hystory.append(n)
  for n in hystory:
    memo[(b, n)] = found
  return found

def FindHappiness(bases):
  n = 1
  while True:
    n += 1
    for b in bases + [-1]:
      if b == -1: return n
      if b == 2: continue
      if not IsHappy(n, b): break

memo = {}
for T in xrange(1, input() + 1):
  print 'Case %d: %d' % (T, FindHappiness(ReadInts()))
