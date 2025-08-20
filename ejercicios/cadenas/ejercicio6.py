"""
Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, 
y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
"""

while True:
    frase = input("Escribe una frase: ")
    vocal = input("Escribe una vocal: ")
    vocal_min = vocal.lower()
    vocal_mayus = vocal_min.upper()
    
    vocales = ["a","e","i","o","u"]

    if vocal_min in vocales:

        nueva_frase = frase.replace(vocal_min, vocal_mayus)

        print(f"Frase modificada:{nueva_frase}")
        break
    else:
        print("Introduce una vocal valida (a,e,i,o,u).")
