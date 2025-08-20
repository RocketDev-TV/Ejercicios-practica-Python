"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla 
la cuenta atrás desde ese número hasta cero separados por comas.
"""

numero = int(input("Escribe el numero por el que deseas empezar: "))

for i in range (numero, -1, -1):
    print(f"{i},",end="")