#Calcolo un semplice moto rettilineo uniforme

x0 = float(input('Immettere coordinata posizione iniziale:    '))
v  = float(input('Immettere velocità (costante) del moto:     '))
t  = float(input("Immettere la durata dell'interv. temporale: "))
x = v*t + x0
print("Il m.r.u. termina in x(t) = ",x,"\n")

#Calcolo un semplice moto rettilineo uniformemente accelerato

x0 = float(input('Immettere coordinata posizione iniziale:    '))
v0 = float(input('Immettere velocità iniziale del moto:       '))
a = float( input('Immettere accelerazione (cost.) del moto:   '))
t  = float(input("Immettere la durata dell'interv. temporale: "))
x =  .5 * a * t**2 + v*t + x0
print("Il m.r.u.a. termina in x(t) = ",x)