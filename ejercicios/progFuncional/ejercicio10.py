"""
Una inmobiliaria de una ciudad maneja una lista de inmuebles como la siguiente:

[{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
{'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
{'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
{'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
{'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]

Construir una función que permita hacer búsqueda de inmuebles en función de un presupuesto dado. 
La función recibirá como entrada la lista de inmuebles y un precio, y devolverá otra lista con los 
inmuebles cuyo precio sea menor o igual que el dado. 
Los inmuebles de la lista que se devuelva deben incorporar un nuevo par a cada diccionario con el 
precio del inmueble, donde el precio de un inmueble se calcula con las siguiente fórmula en función de la zona:

Zona A: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100)
Zona B: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100) * 1.5

"""

# Lista dada
lista = [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
{'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
{'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
{'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
{'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]

# Funcion
def busqueda_inmueble(lista_in, precio_maximo):
    lista_busqueda = []

    for inmueble in lista_in:
        antiguedad = 2025 - inmueble['año']
        base = (inmueble['metros'] * 1000 + 
                inmueble['habitaciones'] * 5000 + 
                inmueble['garaje'] * 15000)
        
        if inmueble['zona'] == 'A':
            precio = base * (1 - antiguedad / 100)
        elif inmueble['zona'] == 'B':
            precio = base * (1 - antiguedad / 100) * 1.5
        else:
            continue  # Por si aparece una zona desconocida

        if precio <= precio_maximo:
            inmueble_con_precio = inmueble.copy()
            inmueble_con_precio['precio'] = round(precio, 2)
            lista_busqueda.append(inmueble_con_precio)

    return lista_busqueda

res = busqueda_inmueble(lista,100000)
for r in res:
    print(r)


