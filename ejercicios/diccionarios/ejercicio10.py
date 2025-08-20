"""
Escribir un programa que permita gestionar la base de datos de clientes de una empresa. 
Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, 
y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), 
donde preferente tendrá el valor True si se trata de un cliente preferente. 
El programa debe preguntar al usuario por una opción del siguiente menú: 
(1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, 
(4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. 
En función de la opción elegida el programa tendrá que hacer lo siguiente:

Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
Preguntar por el NIF del cliente y mostrar sus datos.
Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
Terminar el programa.

"""

dicc_1 = {}

while True:
    print("Menu.\n(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n"
    "(4) Listar todos los clientes\n(5) Listar clientes preferentes\n(6) Terminar")

    opcion = int(input("Elige una opcion: "))

    # Añadir cliente"
    if opcion == 1:
        print("Añadir cliente")
        NIF = input("Ingresa el NIF del cliente:")
        nombre = input("Ingresa el nombre del cliente:") 
        direccion = input("Ingresa la direccion del cliente:") 
        telefono = input("Ingresa el telefono del cliente:") 
        correo = input("Ingresa el correo del cliente:")
        preferente = int(input("Ingresa el tipo de preferencia del cleinte\n(1) con preferencia | (2) sin preferencia:"))
        pref = True if preferente == 1 else False
        
        dicc_1[NIF] = {
            "nombre": nombre,
            "direccion": direccion,
            "telefono": telefono,
            "correo": correo,
            "preferente": pref
        }

        print("El cliente a sido agregado con exito.")

    # Eliminar cliente
    elif opcion == 2:
        print("Eliminar cliente")
        busqueda_eliminar = input("Ingresa el NIF del cliente que deseas eliminar:")
        if busqueda_eliminar in dicc_1:
            del dicc_1[busqueda_eliminar]
            print(f"Cliente {busqueda_eliminar} eliminado con exito.")
        else:
            print("El cleinte no existe en la base de datos.")

    # Mostrar cliente
    elif opcion == 3:
        print("Mostrar cliente")
        busqueda_mostrar = input("Ingresa el NIF del cliente que deseas buscar:")
        if busqueda_mostrar in dicc_1:
            cliente = dicc_1[busqueda_mostrar]
            print(f"Cliente {busqueda_mostrar}")
            print(f"Nombre = {cliente['nombre']}")
            print(f"Direccion = {cliente['direccion']}")
            print(f"Correo = {cliente['correo']}")
            print(f"Telefono = {cliente['telefono']}")
            print(f"Preferente: {'Sí' if cliente['preferente'] else 'No'}")
        else:
            print("El cleinte no existe en la base de datos.")
    
    # Listar todos los clientes.
    elif opcion == 4:
        print("Lista de todos los clientes:\n")
        if dicc_1:
            for nif, cliente in dicc_1.items():
                print(f"  NIF: {nif}")
                print(f"  Nombre: {cliente['nombre']}")
                print(f"  Dirección: {cliente['direccion']}")
                print(f"  Teléfono: {cliente['telefono']}")
                print(f"  Correo: {cliente['correo']}")
                print(f"  Preferente: {'Sí' if cliente['preferente'] else 'No'}")
                print("-" * 40)
        else:
            print("No hay clientes registrados.")

    # Clientes preferentes
    elif opcion == 5:
        print("Listar clientes preferentes")
        preferentes = {nif: c for nif, c in dicc_1.items() if c["preferente"]}
        if preferentes:
            for nif, cliente in preferentes.items():
                print(f"NIF: {nif} - Nombre: {cliente['nombre']}")
        else:
            print("No hay clientes preferentes.")
    # Salir
    elif opcion == 6:
        print("Salir")
        break
    else:
        print("Opcion invalida, por favor intentalo de nuevo.")
    
    continuar = input("¿Deseas relizar otra operacion? (S/N): ").upper()
    if continuar != 'S':
        print("Gracias por usar nuestro sistema.")