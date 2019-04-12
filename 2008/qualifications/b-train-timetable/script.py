for case in xrange(input()):
  tt = int(input())
  trips_a, trips_b = raw_input().split()
  journeys = [raw_input().replace(':', '').split()
              for i in xrange(int(trips_a) + int(trips_b))]
  
  table = []
  for i, journey in enumerate(journeys):
    if i < int(trips_a):
      table.append((int(journey[0][0:2])*60 + int(journey[0][2:]), 'A-'))
      table.append((int(journey[1][0:2])*60 + int(journey[1][2:]) + tt, 'B+'))
    else:
      table.append((int(journey[0][0:2])*60 + int(journey[0][2:]), 'B-'))
      table.append((int(journey[1][0:2])*60 + int(journey[1][2:]) + tt, 'A+'))
  table.sort()

  start_a, start_b = 0, 0
  curr_a, curr_b = 0, 0
  for time, action in table:
    if action == 'A-':
      if not curr_a:
        start_a += 1
      else:
        curr_a -= 1
    elif action == 'A+':
      curr_a += 1
    elif action == 'B-':
      if not curr_b:
        start_b += 1
      else:
        curr_b -= 1
    elif action == 'B+':
      curr_b += 1

  print 'Case #%d: %s %s' % (case + 1, start_a, start_b)
