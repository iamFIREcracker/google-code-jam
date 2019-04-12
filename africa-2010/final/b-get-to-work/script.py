def ReadInts():
  return map(int, raw_input().split())

def solve(i, memo):
  ls = []
  for employee in memo:
    cars = 0
    seats = 0
    while employee:
      if seats == 0 and employee[-1] == 0:
        print 'Case #%d: IMPOSSIBLE' % (i + 1)
        return
      elif seats == 0:
        seats += employee.pop() - 1
        cars += 1
      else:
        employee.pop(0)
        seats -= 1
    ls.append(cars)
  print 'Case #%d: %s' % (i + 1, ' '.join(map(str, ls)))
      
for i in xrange(input()):
  (N, T) = ReadInts()
  memo = [[] for _ in xrange(N)]
  for j in xrange(input()):
    (h, p) = ReadInts()
    if h == T: continue
    memo[h - 1].append(p)
    memo[h - 1].sort()
  solve(i, memo)
