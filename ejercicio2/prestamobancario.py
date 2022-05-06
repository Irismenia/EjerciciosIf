"""Ejercicio 2
Programa que permita realizar un prestamo bancario"""

ingresos=int(input("Ingrese su sueldo: ")) 
#processing
if ingresos>945200:
    deudas=int(input("¿Tienes deudas? Escriba 0 para no. 1 para si: "))
    if deudas==0:
        print("Se aprueba el prestamo")
    else:
     print("No se aprueba el prestamo")
else:
    print("No se aprueba el prestamo")
