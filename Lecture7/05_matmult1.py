a = [[1,2,3],[4,5,6]]
b = [[7,8],[9,10],[11,12]]

#prodotto scalare fra vett. riga di a e vett. colonna di b
def dot_prod(a,b):
  res = 0
  for i in range(len(a)):
    res = res + a[i]*b[i]
  return res

print(dot_prod(a[0],[b[i][0] for i in range(len(b))]))
print(dot_prod(a[0],[b[i][1] for i in range(len(b))]))

#prodotto fra due matrici definito in maniera "canonica"
def mat_prod1(a,b):
  res = [[] for i in range(len(a))]
  for i in range(len(a)):
    for j in range(len(b[0])):
     res[i].append(dot_prod(a[i],[b[k][j] for k in range(len(b))]))
  return res

print(mat_prod1(a,b))

#prodotto fra due matrici definito in maniera più intelligente
def mat_prod2(a,b):
  return [[sum(x*y for x,y in zip(a_row,b_col)) for b_col in zip(*b)] for a_row in a]

print(mat_prod2(a,b))

#[[1, 2, 3], [4, 5, 6]]
print([x for x in a])
print([x[0] for x in zip(a)])

#[([1, 2, 3],), ([4, 5, 6],)]
#tutto questo anche se zip come oggetto non è una lista, bensì uno <zip object at 0x7....> 
print([x for x in zip(a)])
print(list(zip(a)))

#vedo, tuttavia, che il termine x[1] non è nulla, quindi non contribuisce al prodotto

def mat_scal(k,a):
  for i in range(len(a)):
    for j in range(len(a[0])):
      a[i][j] = a[i][j]*k
  return a

print(mat_scal(1,a))