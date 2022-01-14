#Parte 1:

a = ("Marco", "Luca", "Claudio")
b = ("Giovanna", "Maria", "Anna", "Francesca")
x = zip(a, b)
print(tuple(x))

y = zip(a)
print(tuple(y))

#Si vede che zip() è fatto per coppie di list invece che per singoli, essenzialmente, ma viene adattato al caso di un singolo argomento

print('-------------')
#Parte 2:

coordinate = ['x', 'y', 'z']
value = [3, 4, 5]
result = zip(coordinate, value)
result_list = list(result)

#Mostro che per qualche ragione devo estrarre le coppie ordinate dalla list, ma non so perché
print(result_list)
print(*result_list)

c, v = zip(*result_list)
print('c =', c)
print('v =', v)