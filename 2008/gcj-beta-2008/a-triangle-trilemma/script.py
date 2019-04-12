from math import hypot

for case in xrange(input()):
  x1, y1, x2, y2, x3, y3 = map(int, raw_input().split())

  # collinearity:
  #
  # x2 - x1    x3 - x1
  # ------- == -------  ?
  # y2 - y1    y3 - y1
  #
  # better to avoid the division in order to prevent division by 0 
  if (x2 - x1)*(y3 - y1) == (x3 - x1)*(y2 - y1):
    shape = 'not a'
  else:
    s1 =(x1 - x2)**2 + (y1 - y2)**2
    s2 =(x2 - x3)**2 + (y2 - y3)**2
    s3 =(x3 - x1)**2 + (y3 - y1)**2
    if s1 == s2 or s1 == s3 or s2 == s3:
      shape = 'isosceles'
    else:
      shape = 'scalene'

    # Pythagorean theorem
    if s1 == s2 + s3 or s2 == s1 + s3 or s3 == s1 + s2:
      shape += ' right'

    # law of cosines in general:
    # if one of these conditions is verified, the cosine of the angle should
    # assume a negative values, thus the angle is greater than 90 degrees
    elif s1 > s2 + s3 or s2 > s1 + s3 or s3 > s1 + s2:
      shape += ' obtuse'
    else:
      shape += ' acute'


  print 'Case #%d: %s triangle' % (case + 1, shape)
