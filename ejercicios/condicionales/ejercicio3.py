"""
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
Si el divisor es cero el programa debe mostrar un error.
"""

a = int(input("Introduce el primer numero:"))
b = int(input("Introduce el segundo numero:"))

if b == 0:
    print(f"Introduce un divisor valido, no es posible dividir {a} entre 0.")
else:
    c = a / b
    print(f"Division: {a} / {b} = {c}")