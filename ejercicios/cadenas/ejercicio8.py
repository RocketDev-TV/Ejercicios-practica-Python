"""
Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y 
muestre por pantalla el número de euros y el número de céntimos del precio introducido.
"""

valor = float(input("Dame el precio del artículo: €"))
redondear = round(valor, 2)
n_valor = str(f"{redondear:.2f}").split(".")

print(f"El valor es de: {n_valor[0]} euros con {n_valor[1]} céntimos.")

# Solucion 

precio = input("Introduce el precio del producto con dos decimales:  ")
print(precio[:precio.find('.')], 'euros y', precio[precio.find('.')+1:], 'céntimos.')