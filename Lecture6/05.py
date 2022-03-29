def drawer(a,b):
  print("*"*a)
  for i in range(1,b-1):
    print("*"+" "*(a-2)+"*")
  print("*"*a)

while True:
  sides = input("Immettere base e altezza del rettangolo (interi >= 3 e separati da spazi singoli): ").split(" ")
  try:
    a = int(sides[0])
    b = int(sides[1])
    drawer(a,b)
  except ValueError:
    print("Rileggi la richiesta. Riprova.")

  out = input("Vuoi continuare? ('no' per uscire) :")
  if out == "no":
    break