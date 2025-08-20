"""
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde 
en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, 
vive en <dirección> y su número de teléfono es <teléfono>.
"""

diccionario = {"nombre":"", "edad":"", "direccion":"", "telefono":""}

nombre = input("Escribe tu nombre:")
edad = int(input("Introduce tu edad:"))
direccion = input("Introduce tu direccion")
telefono = input("Introduce tu numero de telefono:")

diccionario.update({"nombre":nombre})
diccionario.update({"edad":edad})
diccionario.update({"direccion":direccion})
diccionario.update({"telefono":telefono})

print(f"{diccionario['nombre']} tiene {diccionario['edad']} años, vive en {diccionario['direccion']} y su número de teléfono es {diccionario['telefono']}.")




