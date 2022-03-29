from random import randint

while True:
  
  x = randint(1,10)
  
  while True:
    
    tenta = input("Quanti tentativi vuoi fare? ")
    
    try:
      
      tenta = int(tenta)
      if tenta > 0:
        break
      else:
        print("OK, è un gioco, ma insomma... Metti un intero positivo, per piacere.")
  
    except ValueError:
      print("Devi scegliere un numero di tentativi intero (e positivo).")

  for i in range(tenta):
    guess = input("Tentativo n. {0}: ".format(i+1))
    try:

      guess = int(guess)
      if guess == x:
        print("Brav@, hai indovinato!")
        break
        #esce dal loop dei tentativi, ma non da quello generale del programma
      else:
        print("Ritenta.")
    except ValueError:
      print("Non conta nemmeno come intero, ma pazienza, conta come tentativo.")