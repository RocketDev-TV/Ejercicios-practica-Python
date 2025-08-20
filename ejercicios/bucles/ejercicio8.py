"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo 
rectángulo como el de más abajo.
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
"""

numero = int(input("Ingresa hasta que numero(impar) deseas que se imprima:"))


for y in range(1,numero+1,2):
    for x in range (y,0,-2):
        print(x, end = "")
    print("")

