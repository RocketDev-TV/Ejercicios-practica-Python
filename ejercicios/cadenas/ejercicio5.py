"""
Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.
"""
# Opcion 1
frase = str(input("Introduce una frase: "))

lst_frase = list(frase)
lst_frase.reverse()

print(''.join(lst_frase))

# Opcion 2

frase2 = str(input("Introduce una frase: "))
print(frase2[::-1])