import math, cmath

#funzione per a complessi
def deltaexp(a):
  c = cmath.exp(a)
  b = math.exp(a.real)
  print(b,c)
  b = (b-c.real)**2+c.imag**2
  print(b)
  return b

print(deltaexp(1+4j))