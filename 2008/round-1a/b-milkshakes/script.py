import sys
from heapq import heappush, heappop
from copy import copy

UNMALTED, MALTED = xrange(0, 1)

def ReadInts(f=sys.stdin, sep=" "):
  return list(map(int, f.readline().strip().split(sep)))

for C in xrange(1, input() + 1):
  print "Case #%d:" % C, 
  N = input()
  guesses = []
  for _ in xrange(input()):
    pref = ReadInts()[1:]
    temp = []
    for i in xrange(0, len(pref), 2):
      (n, t) = pref[i:i + 2]
      if not guesses:
        a = [UNMALTED for i in xrange(N)]
        a[n - 1] = t
        heappush(temp, (int(t == MALTED), a))
      else:
        for (m, g) in guesses:
          if g[n - 1] == NONE:
            ng = copy(g)
            ng[n - 1] = t
            heappush(temp, (m + int(t == MALTED), ng))
          elif g[n - 1] == t:
            heappush(temp, (m, g))
    if temp: guesses = temp
    else:
      print "IMPOSSIBLE"
      break
  else:
    (m, s) = heappop(guesses)
    for t in s:
      if t == NONE: print UNMALTED,
      else: print t,
    print
