#--------------------------------------------------
# sequence = map(int, raw_input().split(','))
# longest = [1 for i in xrange(len(sequence))]
# for i in reversed(xrange(len(sequence) - 1)):
#   value = 1
#   for j in xrange(i, len(sequence)):
#     if sequence[i] < sequence[j]:
#       value = max(value, longest[j] + 1)
#   longest[i] = value
# print longest
#-------------------------------------------------- 

for case in xrange(input()):
  n, m, X, Y, Z = map(int, raw_input().split())
  A = [input() for i in xrange(m)]
  
  limits = []
  for i in xrange(n):
    limits.append(A[i%m])
    A[i%m] = (X*A[i%m] + Y*(i + 1))%Z

  for i in xrange(len(limits)):
    value = 1
    for j in xrange(i, len(sequence)):
      if sequence[i] < sequence[j]:
