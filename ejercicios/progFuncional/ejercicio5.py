""""
Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.
"""

def palabras(frase):
    dicc = {}
    frase_s = frase.split(" ")
    for palabra in frase_s:
        dicc[palabra] = len(palabra)
    return dicc

res = palabras("Hola mundo, esto es una frase.")
print(res)