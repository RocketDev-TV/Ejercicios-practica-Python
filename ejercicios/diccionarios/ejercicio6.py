"""
Escribir un programa que cree un diccionario vacío y lo vaya llenado 
con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) 
que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
"""

datos = {}
retorno = True
while retorno:
    tipo = input("¿Que dato deseas agregar?: ")
    valor = input(f"Escribe el valor para {tipo} = ")
    datos[tipo] = valor
    print(f"Diccionario actualizado.\n{datos}")
    
    retorno = input("¿Deseas agregar mas datos? (S/N):") == "S"


