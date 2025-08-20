"""
Escribir un programa que pregunte el nombre de un producto, su precio y un número de unidades y 
muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos 
enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
"""
# Pedir los datos al usuario
nombre = input("Nombre del producto: ")
precio = float(input("Precio unitario: "))
unidades = int(input("Número de unidades: "))

# Calcular el coste total
coste_total = precio * unidades

# Imprimir la cadena formateada
# {:06.2f} → total de 6 dígitos enteros + 2 decimales = 8 caracteres (con relleno de ceros a la izquierda)
# {:03d} → número entero con 3 dígitos
# {:08.2f} → total de 8 dígitos enteros + 2 decimales = 10 caracteres

print(f"{nombre}: ${precio:09.2f} x {unidades:03d} unidades. Total = ${coste_total:011.2f}")
