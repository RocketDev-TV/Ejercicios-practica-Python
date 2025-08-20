"""
Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla 
el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas 
y otra solo con la primera letra del nombre y de los apellidos en mayúscula. 
El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
"""

nombre = str(input("Por favor escribe tu nombre:"))

nom1 = nombre.lower()
print(f"Nombre en minusuclas: {nom1}")

nom2 = nombre.upper()
print(f"Nombre en MAYUSUCLAS: {nom2}")

nom3 = nombre.title()
print(f"Nombre en formato Title: {nom3}")


# Apoyo: https://chuidiang.org/index.php?title=May%C3%BAsculas_y_min%C3%BAsculas_en_python