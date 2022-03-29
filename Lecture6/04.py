w = True
while w:
  num = input("Immettere un numero intero: ")

  try:
    num = int(num) #se l'utente non immette un intero fallisco nella conversione
    if num > 0:
  
      print("#"*num)
      w = False
      
  except ValueError:
    print("Avevo espressamente chiesto un intero. Riprova: ")