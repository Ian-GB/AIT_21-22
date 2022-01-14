## define Python user-defined #exceptions
#class Error(Exception):
#    """Base class for other #exceptions"""
#    pass

class Negativo(Exception):
    """Raised when the input value is too small"""
    pass

try:

  carote = int(input('Quante carote hai in frigo?\n'))
  if (carote < 0):
    raise Negativo

except ValueError:

  print("Bricconə, non è un numero intero, o perlomeno non l'hai scritto in maniera da renderlo per me intelligibile!")

except Negativo:

  print("Bricconə, non ha senso dire che hai questo numero di carote, dimmi 0 piuttosto!")

else:

  print("Ti credo, perché la risposta è plausibile.")

finally:

  print("In ogni caso, se hai aperto il frigo per controllare, è il caso che tu lo chiuda.")

