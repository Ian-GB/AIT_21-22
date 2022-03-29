disponibili = {
  "Farenheit 451": 10,
  "Zibaldone": 7, 
  "Aristotle's Metaphysics": 5,
  "L'Alchimista": 1,
  "Harry Potter": 2,
  "Cime tempestose": 1
}

esauriti = [] #libri del catalogo che sono in prestito

da_ordinare = {}

esito_convert = {True: "Prestito confermato.", False: "Prestito non eseguito."}

def ordina_prompt(Titolo):
  
  global da_ordinare
  w = True
  while w:
  
    ord = input("Ordinare una copia di {0}? (sì/no): ".format(Titolo))
  
    if ord == "sì":
      
      if Titolo in da_ordinare.keys():
        da_ordinare[Titolo] += 1
      else:
        da_ordinare[Titolo] = 1
      w = False

      print("È stata aggiunta una copia di {0} alla lista per l'ordine.".format(Titolo))
        
    elif ord == "no":

      print("Nessuna copia sarà ordinata.")
      w = False

    # se ord /= "sì" o "no" w resta True e la domanda viene posta nuovamente

def presta_libri(Titolo):
  
  if Titolo in disponibili.keys():
    
    if disponibili[Titolo] == 1:
      disponibili.pop(Titolo)
      esauriti.append(Titolo)
    else:
      disponibili[Titolo] -= 1

    esito = True

  elif Titolo in esauriti:

    print("Tutte le copie sono in prestito.")
    ordina_prompt(Titolo)
    esito = False

  else: #cioè se il titolo non appartiene al catalogo della biblioteca

    print("Il testo non è presente nel catalogo.")
    ordina_prompt(Titolo)
    esito = False

  return esito

while True:
  Titolo = input("Immettere il titolo del libro da prestare o 'sì' per uscire: ")
  if Titolo == "sì":
    print(disponibili)
    print(esauriti)
    print(da_ordinare)
    break
  else:
    outcome = presta_libri(Titolo)
    print(esito_convert[outcome])