"""
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función 
de su respuesta le muestre un menú con los ingredientes disponibles para que elija. 
Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. 
Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
"""

print("Bienvenido a Bella Napoli 🍕")
print("¿Qué tipo de pizza deseas?")
print("1. Vegetariana")
print("2. No vegetariana")

tipo_pizza = input("Respuesta (1/2): ").strip()

ingredientes_vegetarianos = {1: "Pimiento", 2: "Tofu"}
ingredientes_no_vegetarianos = {1: "Peperoni", 2: "Jamón", 3: "Salmón"}

if tipo_pizza == "1":
    print("\nIngredientes disponibles (vegetariana):")
    for key, val in ingredientes_vegetarianos.items():
        print(f"{key}. {val}")

    ingrediente = input("Selecciona el ingrediente (1/2): ").strip()
    if ingrediente in ["1", "2"]:
        ing = ingredientes_vegetarianos[int(ingrediente)]
        print(f"\n🧾 Ticket final:")
        print("Tipo de pizza: Vegetariana")
        print(f"Ingredientes: Mozzarella, tomate y {ing}")
    else:
        print("⚠️ Opción de ingrediente inválida.")

elif tipo_pizza == "2":
    print("\nIngredientes disponibles (no vegetariana):")
    for key, val in ingredientes_no_vegetarianos.items():
        print(f"{key}. {val}")

    ingrediente = input("Selecciona el ingrediente (1/2/3): ").strip()
    if ingrediente in ["1", "2", "3"]:
        ing = ingredientes_no_vegetarianos[int(ingrediente)]
        print(f"\n🧾 Ticket final:")
        print("Tipo de pizza: No vegetariana")
        print(f"Ingredientes: Mozzarella, tomate y {ing}")
    else:
        print("⚠️ Opción de ingrediente inválida.")

else:
    print("⚠️ Tipo de pizza no válido. Intenta nuevamente.")
