"""
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
"""

cadena = input("Introduce la palabra a validar:")

cadena2 = cadena[::-1]

if cadena == cadena2:
    print("Es un palindromo!")
else:
    print("No es un palindromo")
