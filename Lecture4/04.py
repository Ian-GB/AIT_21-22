#Prima parte del codice
def f_sum(a, b):
    sum = a + b
    return sum
a = 1
b = 2
sum = 3
f_sum(100, 100)
print(sum,"\n")

#Seconda parte del codice
def f_sum(a, b):
    sum = a + b
    return sum
a = 1
b = 2
sum = 3
print(f_sum(100, 100))

#La funzione f_sum nella prima parte del codice restituisce 200 in output, ma questo non viene associato a nessuna variabile nel programma, perché la variabile "sum" modificata è locale, non quella globale. Nella seconda parte del codice, invece, viene proprio visualizzato il 200 calcolato nella funzione.