#lettura della matrice da file e studio di come si trasforma

#PARTE 1: Con funzioni di base di Python

l = []
m = []
with open('03_inmatrix1.txt', 'r') as f:
  for line in f:
    line = line.strip()
    if len(line) > 0:

      #list() serve perché l'output di map() non è una lista di per sé, non in Python 3, almeno
      l.append(list(map(int, line.split(','))))

      #senza list() esce un oggetto brutto, se non usi Python 2.x
      m.append(map(int, line.split(',')))

print('Con list():')
print(l)
print('Senza list():')
print(m)

fin = open('03_inmatrix1.txt','r')
a,b=[],[]
for line in fin.readlines():
  a.append( [ int (x) for x in line.split(',') ] )
  b.append( [ int (x) for x in line.replace('\n','').split(',') ] )

print(a)
print(b)

#PARTE 2: Con NumPy

import numpy as np

input = np.loadtxt("03_inmatrix1.txt", dtype='i',
delimiter=',')
print(input)