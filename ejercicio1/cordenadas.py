"""Ejercicio 1
programacion de cordenadas cartesianas"""

X= int(input("Ingrese coordenada en x: "))
Y= int(input("Ingrese coordenada en y: "))
if(X > 0 and Y > 0):
    print("Punto en el primer cuadrante")

elif(X < 0 and Y > 0):
    print("Punto en el segundo cuadrante")

elif (X < 0 and Y < 0):
    print("Punto en el tercer cuadrante")

elif (X > 0 and Y < 0):
    print("Punto en el cuarto cuadrante")    

elif X==0 and Y==0:
    print("El punto esta en el origen")