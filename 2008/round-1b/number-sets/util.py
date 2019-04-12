from math import hypot

"""Generate a list of the integer divisors of the given number
"""
def divisor(n):
    factors = [f for f in factor(n)]
    print factors

"""Generate a list of the factors of the given number
"""
def factor(n):
  yield 1
  i = 2
  limit = n**.5
  while i <= limit:
    if not n%i:
      yield i
      n /= i
      limit = n**.5
    else:
      i += 1
  if n > 1:
    yield n

"""Generate a list of n digits from the Fibonacci serie
"""
def fibonacci(n):
  a, b = 1, 1
  while n:
    yield b
    a, b = b, a + b
    n -= 1

"""Generate a list of digits from the Fibonacci serie: n is the upper bound
"""
def fibonacci1(n):
  a, b = 1, 1
  while b < n:
    yield b
    a, b = b, a + b

"""Generate a list of prime numbers: n is the upper bound
"""
def primes(n):
  if n >= 1:
    yield 2
    n -= 1
    primes = [2]
    i = 3
    while n:
      for p in primes:
        if not i%p or p*p > i:
          break
      if i%p:
        yield i
        primes.append(i)
        n -= 1
      i += 2

"""Generate a list of prime numbers: n is the upper bound
"""
def primes1(n):
  if n >= 2:
    yield 2
    primes = [2]
    for i in xrange(3, n, 2):
      for p in primes:
        if not i%p or p*p > i:
          break
      if i%p:
        yield i
        primes.append(i)

"""Generate a list of the first k Pythagorean triplets
"""
def pythagorean_triplets(k, primitive=True):
  if k >= 1:
    m = 2
    while True:
      for n in xrange(1, m):
        if m%2 and n%2:
          continue
        a, b, c = n, m, hypot(n, m)
        if c != int(c):
          continue
        c = int(c)
        if primitive:
          fa, fb, fc = set(factor(a)), set(factor(b)), set(factor(c))
          if len(fa.intersection(fb.intersection(fc))) != 1:
            continue
        yield a, b, c
        k -= 1
        if not k:
          return
      m += 1


if __name__ == '__main__':
  import sys

  for n in sys.argv[1:]:
    print [f for f in pythagorean_triplets(int(n), False)]
