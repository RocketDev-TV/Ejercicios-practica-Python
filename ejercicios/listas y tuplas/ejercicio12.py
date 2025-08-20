"""
Escribir un programa que almacene las matrices
    
A = 1,2,3
    4,5,6

B =-1,0
    0,1
    1,1

en una lista y muestre por pantalla su producto.
Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.
"""
A = [
    [2, 4, 6],
    [8, 0, 10]
]

B = [
    [1, 3],
    [5, 7],
    [9, 11]
]

resultado = []

for i in range(len(A)):  # filas de A
    fila_resultado = []
    for j in range(len(B[0])):  # columnas de B
        suma = 0
        for k in range(len(A[0])):  # elementos de la fila de A / columna de B
            suma += A[i][k] * B[k][j]
        fila_resultado.append(suma)
    resultado.append(fila_resultado)

print(f"Resultado = {resultado}")
