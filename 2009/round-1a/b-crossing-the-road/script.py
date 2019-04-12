from heapq import heappush, heappop

def ReadInts(f):
  return list(map(int, f.readline().strip().split(" ")))

def ReadSemaphores(f):
  sem = []
  for _ in xrange(N):
    args = ReadInts(f)
    sem.append([(args[i], args[i + 1], args[i + 2])
                for i in xrange(0, len(args), 3)])
  return sem

def CreateHeuristic(N, M):
  h = [[-1 for _ in xrange(2*M)] for _ in xrange(2*N)]
  for i in xrange(2*N):
    for j in reversed(xrange(2*M)):
      if j == 2*M - 1: # last element of a row
        if i == 0: h[i][j] = 0
        elif i%2: h[i][j] = 1 + h[i - 1][j]
        else: h[i][j] = 2 + h[i - 1][j]
      else:
        if not j%2: h[i][j] = 1 + h[i][j + 1]
        else: h[i][j] = 2 + h[i][j + 1]
  return h

f = open('test')
for case in xrange(1, int(f.readline()) + 1):
  (N, M) = ReadInts(f)[0:2]
  sem = ReadSemaphores(f)

  g = [[0 for _ in xrange(2*M)] for _ in xrange(2*N)]
  h = CreateHeuristic(N, M)

  open = [(g[-1][0] + h[-1][0], 0, 0)]
  close = [[0 for _ in xrange(2*M)] for _ in xrange(2*N)]
  while open:
    (f, i, j) = heappop(open)
    if (i, j) == (0, 2*M - 1):
      print g[i][j]
      break
    for (nt, nj) in Neighbors(i, j, N, N):
      ng = g[i][j] + nt
      if not g[ni][nj] or ng < g[ni][nj]:
        g[ni][nj] = ng
        nf = ng + h[i][j]
        close[ni][nj] = nf
        heappush(open, (nf, ni, nj))
    close[i][j] = f
  print "Case #%d" % case 
