import numpy as np

#manipoliamo due array della medesima lunghezza
x = np.linspace(0,3.7*np.pi,7)
b = np.sin(x)**2+np.cos(x)**2
print(b)

#manipoliamo due array di diversa lunghezza: non funziona
#a = 3.7
#x = np.linspace(0,a*np.pi,7)
#y = np.linspace(0,2*a*np.pi,14)
#b = np.sin(x)**2+np.cos(y)**2
#print(b)

#manipoliamo due array di diversa lunghezza: non funziona
a = 3.7
x = np.linspace(0,a*np.pi,7)
y = np.linspace(0,2*a*np.pi,14)
b = np.sin(x)**2+np.cos(y)**2
print(b)