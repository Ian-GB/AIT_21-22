#PARTE 1: contatore di comparse di caratteri in stringa

def occur(string):

  counts = {}
  
  while len(string) != 0:
    
    counts[string[0]] = string.count(string[0])
    string = string.replace(string[0],"")
  
  return counts

strg = input("Immettere la stringa da analizzare:\n")
print(occur(strg))

#PARTE 2: contatore di comparse di caratteri in file

file = open("03_LI.txt")
lines = file.readlines()
file.close()

filecnts = []

for i in range(len(lines)):
  lines[i] = lines[i].replace("\n","")
  cnts = occur(lines[i])
  print("Riga n. {0}:".format(i+1))
  for j in cnts.keys() :
    print("{0}\t".format(j),"*"*cnts[j])