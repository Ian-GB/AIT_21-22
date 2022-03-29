def passingby(item, list):
  if item in list:
    inx = list.index(item)
  else:
    inx = None
  return inx

type = input("Immettere il tipo di variabile degli elementi della lista: ")
item = eval(type+'(input("Immettere elemento: "))')
list = input("Immettere lista, cone gli elementi separati da spazi singoli: ").split(" ")
for i in range(len(list)):
  list[i] = eval(type+'(list[i])')
print(passingby(item, list))