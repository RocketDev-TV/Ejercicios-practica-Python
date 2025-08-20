"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo 
como el de más abajo, de altura el número introducido.
*
**
***
****
*****
"""

altura = int(input("Ingresa el valor de la altura de el triangulo:"))

for y in range(altura):
    for x in range(y+1):
        print("*", end= "")
    print("")