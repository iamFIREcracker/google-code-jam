def ReadInts():
  return list(map(int, raw_input().strip().split(" ")))

for case in xrange(1, input() + 1):
  (n, k) = ReadInts()
  charts = []
  for i in xrange(n):
    p = ReadInts()
    if not i:
      charts.append([p])
      continue
    for j in xrange(len(charts)):
      for c in charts[j]:
        print p, c, charts[j]
        for (k, (nv, cv)) in enumerate(zip(p, c)):
          if nv == cv: break
          if not k:
            if nv > cv: over = True
            else: over = False
          else:
            if not over and nv > cv: break
            elif over and nv < cv: break
        else: continue
        break
      else:
        charts[j].append(p)
        break
    else:
      charts.append([p])

  print "Case #%d: %d" % (case, len(charts))
