"""
Escribir un programa que gestione las facturas pendientes de cobro de una empresa. 
Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura 
y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, 
pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y 
su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y 
se eliminará del diccionario. 
Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la 
cantidad pendiente de cobro.
"""

facturas = {}
cobrado = 0.0

while True:
    print("Sistema de facturadcion.\n1.-Añadir factura\n2.-Pagar factura\n3.-Salir")
    opcion = int(input("Ingresa la opcion que deseas consultar:"))

    if opcion == 1:
        print("Añadir factura")
        n_fac = int((input("Ingresa el numero de la factura:")))
        costo_fac = float(input("Ingresa el valor de la factura a pagar: $"))
        facturas[n_fac] = costo_fac
        print("Factura agregada con exito!.")
        print(f"Facturas: {facturas}")

    elif opcion == 2:
        print("Pagar factura")
        buscar = int(input("Ingresa el numero de factura que deseas pagar:"))
        if buscar in facturas:
            cobrado += facturas[buscar]
            del facturas[buscar]

            print("Factura paga con exito!.")
            print(f"Facturas: {facturas}")
        else:
            print("El numeor de factura ingresado no existe en el sistema, por favor intentalo de nuevo.")

    elif opcion == 3:
        print("Gracias por usar nuestro sistema.")
        break
    else:
        print("Opcion invalida, por favor intentalo de nuevo.")

    pendiente = sum(facturas.values())
    print(f"Total cobrado hasta el momento: ${cobrado:.2f}")
    print(f"Total oendiente hasta el momento: ${pendiente:.2f}")
    
    continuar = input("¿Deseas relizar otra operacion? (S/N): ").upper()
    if continuar != "S":
        print("Gracias por usar nuestro sistema.")
        break
