"""
Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo 
es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). 
Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla 
el número de teléfono sin el prefijo y la extensión.
"""

while True:
    numero = input("Escribe tu numero telefonico\ncon formato(+00-000000000-00)):")
    valor = 16
    if len(numero) == valor:
        numero_separado = numero.split("-")
        print(f"El numero introducido es:{numero_separado[1]}")
        break
    else: 
        print("Debes introducir un numero valido.")

