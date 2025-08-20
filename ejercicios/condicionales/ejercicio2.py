"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario 
por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada 
en la variable sin tener en cuenta mayúsculas y minúsculas.
"""

# Guardamos la contraseña base
contrasena_guardada = input("Define tu contraseña: ").strip().lower()

while True:
    print("\n---- LOGIN ----")
    intento = input("Introduce la contraseña: ").strip().lower()

    if intento == contrasena_guardada:
        print("Bienvenido al sistema :)")
        break
    else:
        print("Contraseña inválida, por favor vuelve a intentarlo.")
