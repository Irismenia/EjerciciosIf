"""Ejercicio 3
Programa que le indique un precio de venta al articulo dado"""

#input

preciocosto= float(input("Dame el precio de costo del articulo: "))

#Processing

if preciocosto<3000:
    ganancia= preciocosto * 0.15
else:
    if preciocosto<=6000:
        ganancia=500
    else:
        ganancia= preciocosto * 0.25 

precio_venta=preciocosto+ganancia

#output

print(str(preciocosto) + " más la ganancia que es " + str(ganancia) + " da " + str(precio_venta))
