"""
Escribir un programa que cree un diccionario simulando una cesta de la compra. 
El programa debe preguntar el artículo y su precio y añadir el par al diccionario, 
hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, 
con el siguiente formato:

Lista de la compra	
Artículo 1	Precio
Artículo 2	Precio
Artículo 3	Precio
…	…
Total	Coste
"""

cesta = {}
total = 0

while True:
    # Llenar el diccionario 'cesta'
    articulo = input("Introduce el nombre del artículo que deseas agregar: ")
    precio = float(input(f"Introduce el precio de {articulo}: $"))
    cesta[articulo] = precio
    total += precio

    # Preguntamos por el retorno
    continuar = input("¿Deseas agregar más artículos? (S/N): ").upper()

    if continuar != "S":
        print("\n[+] Lista de compras [+]")
        for val, prec in cesta.items():
            print(f"Artículo = {val} | Precio = ${prec:.2f}")
        print(f"Total = ${total:.2f}")
        break


