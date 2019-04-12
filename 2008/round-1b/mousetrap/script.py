from collections import deque

for case in xrange(input()):
  cards = input()
  indexes = map(int, raw_input().split())

  deck = [0 for i in xrange(cards)]
  index = -1
  for i in xrange(1, cards + 1):
    while True:
      index = (index + 1)%cards
      if deck[index] == 0:
        break
    for j in xrange(i - 1):
      while True:
        index = (index + 1)%cards
        if deck[index] == 0:
          break
    deck[index] = i


#--------------------------------------------------
# for case in xrange(input()):
#   k = input()
#   indexes = map(int, raw_input().split())
# 
#   deck = deque()
#   for card in xrange(k, 0, -1):
#     deck.appendleft(card)
#     print deck
#     deck.rotate(card - 1)
#     print deck
#-------------------------------------------------- 
      
  print 'Case #%d: %s' % (case + 1, ' '.join(str(deck[i - 1])
                                                 for i in indexes[1:]))
