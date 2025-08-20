"""
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
calcule el índice de masa corporal y lo almacene en una variable, y muestre por 
pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice 
de masa corporal calculado redondeado con dos decimales.
"""

# Formula IMC = peso (kg) / estatura²(m)

peso = int(input("Ingresa el peso en kg:"))
estatura = float(input("Ingresa la altura en metros:"))

IMC = peso / (estatura**estatura)

print(f"Tu IMC es: {IMC}")

if IMC < 18.5:
    print("Estas bajo de peso.")
elif IMC > 18.5 and IMC < 24.9:
    print("Estas en tu peso ideal.")
elif IMC > 25 and IMC < 29.9:
    print("Tienes sobre peso.")
else:
    print("Sobre peso tipo 1.")