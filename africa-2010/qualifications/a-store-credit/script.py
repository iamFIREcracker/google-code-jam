for i in xrange(input()):
  budget = input()
  input()
  memo = {}
  for (j, price) in enumerate(map(int, raw_input().split())):
    if price < budget:
      if budget - price in memo:
        print 'Case #%d: %d %d' % (i + 1, memo[budget - price], j + 1)
        break
      memo[price] = j + 1
