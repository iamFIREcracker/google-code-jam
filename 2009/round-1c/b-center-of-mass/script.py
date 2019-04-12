import math

def ReadInts():
  return list(map(int, raw_input().strip().split(" ")))

def Distance(com, t):
  (x, y, z, vx, vy, vz) = com
  x = x + t*vx
  y = y + t*vy
  z = z + t*vz
  return math.sqrt(sum(map(lambda v: v*v, [x, y, z])))

for case in xrange(input()):
  N = input()
  f = [ReadInts() for _ in xrange(N)]
  com = [sum(float(f[i][j]) for i in xrange(N))/N for j in xrange(6)]

  # ternary search
  (l, r) = (0.0, 1e15)
  if com[3] == 0 and com[4] == 0  and com[5] == 0: r = 0
  while r - l  > 1e-8:
    ll = (l + l + r)/3
    rr = (l + r + r)/3
    dl = Distance(com, ll)
    dr = Distance(com, rr)
    if (dl < dr): r = rr
    else: l = ll
  print "Case #%d: %.8f %.8f" % (case + 1, Distance(com, l), l)
