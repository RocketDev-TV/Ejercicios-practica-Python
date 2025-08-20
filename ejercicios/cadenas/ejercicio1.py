"""
Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima 
por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
"""

nombre = str(input("Escribe tu nombre:"))
numero = int(input("Escribe el numero de repeticiones:"))

for i in range(1,numero+1):
    print(f"{i}.-Hola!, mucho gusto {nombre}")
