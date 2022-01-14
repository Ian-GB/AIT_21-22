import math

def f(y):
  if y >= 0.0:
    return y**5*math.exp(-y)
  else:
    return 0.0

#PARTE 1
#Legge le righe di infile, e per ciascuna trasforma il secondo termine in base al primo, quindi salva su file la tabella dei valori primo originale e secondo trasformato

infile='02_mydata.dat'
outfile='02_myout.dat'

indata = open(infile, 'r')
linee=indata.readlines()
indata.close()
processati=[ ]
x=[ ]
for el in linee:
  valori = el.split()
  x.append(float(valori[0])); y = float(valori[1])
  processati.append(f(y))

outdata = open(outfile, 'w')
i=0
for el in processati:
  outdata.write('%g %12.5e\n' % (x[i],el))
  i+=1
outdata.close()

#PARTE 2
#Cerca la stringa "DB_DATABASE=" in ciascuna riga del file

file = open('02_.env', "r")
filecontent = file.read()
print("File content:")
print(filecontent)
my_line = ""
for line in filecontent.splitlines():
  print("Working on line", line)
  if line.find("DB_DATABASE="):
    print("Found line containing 'DB_DATABASE='")
    break