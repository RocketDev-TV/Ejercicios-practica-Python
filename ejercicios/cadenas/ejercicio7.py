"""
Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por 
pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.
"""
# Opcion 1
correo = str(input("Introduce tu correo electronico:"))

correo_separado = correo.split("@")
correo_posicion = correo_separado[1]
correo_nuevo = correo.replace(correo_posicion,"ceu.es")

print(f"El correo nuevo es:{correo_nuevo}")

# Opcion 2

email = input("Introduce tu correo electrónico: ")
print(email[:email.find('@')] + '@ceu.es')
