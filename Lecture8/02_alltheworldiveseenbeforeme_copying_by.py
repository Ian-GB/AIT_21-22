import numpy as np

#vincola a e b alla stessa posizione di memoria, ma lascia cambiare i due array
a = np.arange(5)
b = a
b[0]=100
print ("a:", a , "b:" , b)

#vincola a e b alla stessa posizione di memoria
a = np.arange(5)
b = a
#ma questa operazione, termine a termine con un ciclo implicito,
#sugli oggetti che sono le componenti dell'array
#non cambia gli array
b[:] = b[:] + 0.5
print('b:',b,'a:',a)
#mentre questa lo fa, su un oggetto che è l'array
b = b + 0.5
print('b:',b,'a:',a)