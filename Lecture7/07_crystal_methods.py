#Definisco una classe e creo un metodo che varia in base all'input, tanto è una funzione, quindi posso farci quello che farei con una funzione

class Person_mood:
  def __init__(self, name, age, mood):
    self.name = name
    self.age = age
    self.mood = mood
  def intro(self):
    if (self.mood == 'bad'):
      print("Hello, my name is " + self.name + ".")
    if (self.mood == 'good'):
      print("Hello, my name is not anything other than " + self.name + ", and I shall not respond if called otherwise.")

Ian = Person_mood("Ian",23,"good")
Ian.intro()