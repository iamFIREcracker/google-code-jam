def purge(operators, sequence):
  seq = ''
  for i, value in enumerate(zip([''] + operators, sequence)):
    o, d = value
    seq += o 
    if i != len(sequence) - 1 and d == '0' and o in '+-':
      continue
    seq += d
  return seq

def generate(sequence):
  l = len(sequence) - 1
  sequence = [c for c in sequence]
  operators = ['' for i in xrange(l)]
  yield purge(operators, sequence)
  for n in xrange(3**(l) - 1):
    i = l - 1
    while True:
      if operators[i] == '-':
        operators[i] = ''
        i -= 1
        continue
      elif operators[i] == '+':
        operators[i] = '-'
      else:
        operators[i] = '+'
      break
    yield purge(operators, sequence)


for case in xrange(input()):
  expressions = 0
  for sequence in generate(raw_input()):
    if not sequence:
      expressions += 1
      continue
    #n = eval(sequence)
    #if not n%2 or not n%3 or not n%5 or not n%7:
    #  expressions += 1
  print 'Case #%d: %d' % (case + 1, expressions) 
