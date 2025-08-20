"""
Escribir una función que reciba una muestra de números y devuelva los valores atípicos, es decir, los 
valores cuya puntuación típica sea mayor que 3 o menor que -3. 
Nota: La puntuación típica de un valor se obtiene restando la media y dividiendo por la desviación 
típica de la muestra.
"""
import statistics

def valores_atipicos(lista):
    atipicos = []
    media = statistics.mean(lista)
    desv = statistics.stdev(lista)

    for valor in lista:
        z_score = (valor - media) / desv
        if z_score > 3 or z_score < -3:
            atipicos.append(valor)

    return atipicos

datos = [10, 12, 14, 13, 15, 16, 11, 500]
print(valores_atipicos(datos))