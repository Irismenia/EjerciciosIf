"""Ejercicio 5
Calcular el gasto de agua de una vivienda dado el número de m2 de agua
gastados"""

#input
from re import X


metros_gastados=int(input("Digite los metros gastados: "))

if metros_gastados<=50:
    costo_agua=10000
    print("el costo seria " + str(costo_agua))
elif metros_gastados<=200:
    costo_agua=10000+2000*(metros_gastados -50)
    print("el costo seria " + str(costo_agua))
else:
    costo_agua=10000+3000*(metros_gastados -50)
    print("el costo seria " + str(costo_agua))