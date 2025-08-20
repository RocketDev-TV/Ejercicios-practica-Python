"""
Escribir una función que simule una calculadora científica que permita calcular el seno, coseno, tangente, exponencial y logaritmo neperiano. 
La función preguntará al usuario el valor y la función a aplicar, y mostrará por pantalla una tabla con los enteros de 1 al valor introducido 
y el resultado de aplicar la función a esos enteros.
"""
#Librerias
import math

# Funciones
def cal_sen(valor):
    return math.sin(valor)

def cal_cos(valor):
    return math.cos(valor)

def cal_tan(valor):
    return math.tan(valor)

def cal_exp(valor,exp):
    return pow(valor,exp)
    
def cal_log(valor):
    return math.log(valor) 


while True:
    # Menu principal
    opcion = int(input("[+---Calculadora---+]\n1.-Seno\n2.-Coseno\n3.-Tangente\n4.-Exponencial\n5.-Logaritmo natural\nRespuesta = "))

    if opcion == 1:
        print("Seno")
        num = int(input("Ingresa el numero a calcular:"))
        for i in range(1,num+1):
            print(f"Seno de {i} = {cal_sen(i):.2f}")
        
    elif opcion == 2:
        print("Coseno")
        num_2 = int(input("Ingresa el numero a calcular:"))
        for i in range(1,num_2+1):
            print(f"Coseno de {i} = {cal_cos(i):.2f}")
            
    elif opcion == 3:
        print("Tangente")
        num_3 = int(input("Ingresa el numero a calcular:"))
        for i in range(1,num_3+1):
            print(f"Tangente de {i} = {cal_tan(i):.2f}")
            
    elif opcion == 4:
        print("Exponencial")
        num_4 = int(input("Ingresa el numero a calcular:"))
        exponente = int(input("Ingresa el exponente:"))
        
        for i in range(1,num_4+1):
            print(f"Base {i} elevado a la {exponente} potencia = {cal_exp(i,exponente):.2f}")
            
    elif opcion == 5:
        print("Logaritmo natural")
        num_5 = int(input("Ingresa el numero a calcular:"))
        if num_5 >= 1:
            for i in range(1, num_5 + 1):
                print(f"Logaritmo natural de {i} = {cal_log(i):.2f}")
        else:
            print(f"Logaritmo no definido para {num_5}")

    else:
        print("Opcion invalida, por favor intentalo de nuevo.")
    
    continuar = input("¿Deseas relizar otra operacion? (S/N): ").upper()
    if continuar != "S":
        print("Gracias por usar nuestro sistema.")
        break