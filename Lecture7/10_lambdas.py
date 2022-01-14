#sum over array
sum = lambda x,y: x+y
a = sum(4,5)
print(a)

intlist = lambda arr: [int(i) for i in arr]
b = intlist('67,65,35,87'.split(','))
print(b)
#lambda is just a coincise way of defining a function