"""
Escribir un programa en el que se pregunte al usuario por una frase y una letra, 
y muestre por pantalla el número de veces que aparece la letra en la frase.
"""

"""
Escribir un programa en el que se pregunte al usuario por una frase y una letra, 
y muestre por pantalla el número de veces que aparece la letra en la frase.
"""

frase = input("Ingresa una frase:")
letra = input("Ingresa la letra a buscar:")

contador = 0

for caracter in frase:
    if caracter == letra:
        contador += 1

print(f"La letra {letra} Total {contador}")
# for i in range(1, len(frase)+1):
