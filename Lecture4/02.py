#Dichiaro alcune variabili usando già il typecasting esplicito
int1 = 13
int2 = int(51.0)
flt1 = 53.7
flt2 = complex(-3.41,6).real
com1 = 4. + 3.j
com2 = complex("-5+7.j")
boo1 = bool(3) #-> True
boo2 = False
str1 = "j"
str2 = str(4.+3.j)

#Operazioni fra int
print("\nOperazioni fra int")
print("somma:\t\t", int1+int2)
print("differenza:\t", int1-int2 )
print("modulo:\t\t", int1%int2 )

#Operazioni fra float
print("\nOperazioni fra float")
print("somma:\t\t", flt1+flt2)
print("divisione:\t", flt1/flt2 )

#Operazioni fra complessi
print("\nOperazioni fra complessi")
print("somma:\t\t", com1+com2)
print("divisione:\t", com1/com2 )

#Operazioni fra booleani
print("\nOperazioni fra booleani")
print("AND:\t\t", boo1 and boo2)
print("OR:\t\t\t", boo1 or boo2 )
print("NAND:\t\t", not(boo1 and boo2 ))

#Operazioni fra stringhe
print("\nOperazioni fra stringhe")
print("'Somma':\t", str2+str1*6)
print("'Sottrazione':", str2.replace(str1,''))
#print("NAND:\t\t", not(boo1 and boo2 ))

#Typecasting implicito
print("\nOperazioni logiche su numeri")
print("AND fra numeri - secondo dei due numeri (primo numero diverso da 0):")
print("51 - (13 and 51):\t",int2 - (int1 and int2))
print("AND fra numeri - secondo dei due numeri (primo numero 0):")
print("51 - (0 and 51):\t",int2 - (0 and int2))
print("NOT(com1):\t", not(com1))
print("NOT(-1):\t", not (-1) )
#essenzialmente il valore logico di un numero consiste nel suo essere non nullo
print("13 + True:\t",13 + True)

print("\nOperazioni fra numeri di tipi diversi")
print("13+53.7:\t", int1+flt1)
print("53.7 + 4+3j:", flt1+com1)