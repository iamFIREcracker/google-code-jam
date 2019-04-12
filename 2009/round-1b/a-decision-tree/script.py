def Child1(desc, i):
  return i + 2

def Child2(desc, i):
  count = 0
  for d in desc[i + 1:]:
    if d == '(': count += 1
    elif d == ')': count -= 1
    i += 1
    if count == 0: return i + 2 

for N in xrange(1, input() + 1):
  L = input()
  desc = ''.join(raw_input().replace('(', ' ( ').replace(')', ' ) ')
                 for _ in xrange(L)).split()

  A = input()
  print('Case #%d:' % N)
  for _ in xrange(A):
    quals = raw_input().split()[2:]

    pro = 1.0
    i = 1
    while True:
      pro *= float(desc[i])
      if desc[i + 1].isalpha():
        if desc[i + 1] in quals:
          i = Child1(desc, i + 1)
        else:
          i = Child2(desc, i + 1)
      else:
        print('%.6f' % pro)
        break
