"""
Escribir un programa que cree un diccionario de traducción español-inglés. 
El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> 
separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. 
Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. 
Si una palabra no está en el diccionario debe dejarla sin traducir.
"""

diccionario = {}
traduccion = []

while True:
    palabra = input("Introduce la palabra que deseas agregar en el siguiente formato (palabra:traducción) = ")
    if ":" not in palabra:
        print("Formato incorrecto. Usa el formato palabra:traducción.")
        continue

    palabra_separada = palabra.split(":")
    diccionario[palabra_separada[0].lower()] = palabra_separada[1]

    continuar = input("¿Deseas agregar más palabras? (S/N): ").upper()
    if continuar != "S":
        frase = input("Introduce la frase que deseas traducir: ")
        frase_separada = frase.split(" ")

        for palabra in frase_separada:
            # Eliminar puntuacion antes de buscar en el diccionario
            palabra_limpia = palabra.strip(",.!?").lower()

            if palabra_limpia in diccionario:
                traduccion.append(diccionario[palabra_limpia])
            else:
                traduccion.append(palabra)

        print(" ".join(traduccion))
        break