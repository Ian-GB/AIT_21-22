import sys

#Prende intero e lettera in input dall'utente e dichiara di usarli

while(True):
  print('PLEASE INSERT AN INTEGER NUMBER IN THE RANGE 0-10')
  param1 = input()
  if int(param1) in range(11):
    while(True):
      print( 'PLEASE INSERT A CHAR PARAMETER IN [A,B,C]')
      param2 = input()
      if param2 in ['A','B','C']:
        print('uso I due parametri passati dall utente: ',param1,param2)
        sys.exit()
      else: print('TRY AGAIN PLEASE')
  else: print('TRY AGAIN PLEASE')