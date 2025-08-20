"""
Escribir una función reciba un diccionario con las asignaturas y las notas de un alumno y 
devuelva otro diccionario con las asignaturas en mayúsculas y las calificaciones correspondientes 
a las notas aprobadas.
"""

def transformacion(diccionario):
    dicc_n = {}

    for materia,nota in diccionario.items():
        if nota >= 6 and nota < 8:
            dicc_n[materia.upper()] = "Calif. baja"
        elif nota >= 8 and nota < 9:
            dicc_n[materia.upper()] = "Calif. regular"
        elif nota >= 9:
            dicc_n[materia.upper()] = "Calif. buena"
    
    return dicc_n

dicc = {
    'Matematicas': 10,
    'Fisica': 8,
    'Ingles': 5
}

res = transformacion(dicc)
print(res)