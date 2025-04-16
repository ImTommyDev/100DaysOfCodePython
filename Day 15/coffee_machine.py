from data import recursos_disponibles, sabores_cafe, valor_monedas
import os

maquina_encendida = True
pedir = False

# Función para limpiar la consola
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para mostrar los recursos de la máquina
def mostrar_recursos():
    limpiar_pantalla()
    print("══════════════════════════════════════")
    print("     📊 Recursos actuales de la máquina")
    print("══════════════════════════════════════")
    for recurso, cantidad in recursos_disponibles.items():
        print(f"🔹 {recurso.capitalize()}: {cantidad}")
    print("══════════════════════════════════════")
    input("Presiona enter para continuar...")

# Función para asegurar que el usuario ingrese solo números
def obtener_moneda(mensaje):
    while True:
        entrada = input(mensaje)
        if entrada.isdigit():
            return int(entrada)
        else:
            print("⚠️  Por favor, introduce un número válido.")

# Función principal para pedir un café
def pedir_cafe():
    limpiar_pantalla()

    print("☕ ¿Qué tipo de café deseas?")
    print("  1 - Espresso")
    print("  2 - Latte")
    print("  3 - Cappuccino")
    print("══════════════════════════════════════")

    tipo_cafe = input("Elige una opción (1/2/3): ")
    if tipo_cafe not in ["1", "2", "3"]:
        print("❌ Opción no válida.")
        input("Presiona enter para continuar...")
        return True

    nombre_cafe = { "1": "Espresso", "2": "Late", "3": "Cappuccino" }[tipo_cafe]
    ingredientes_cafe = sabores_cafe[nombre_cafe]["ingredientes"]
    precio_cafe = sabores_cafe[nombre_cafe]["precio"]

    # Verificar disponibilidad de recursos
    for ingrediente in ingredientes_cafe:
        if ingredientes_cafe[ingrediente] > recursos_disponibles[ingrediente]:
            print(f"🚫 No hay suficiente {ingrediente} para preparar un {nombre_cafe}.")
            input("Presiona enter para continuar...")
            return False

    # Solicitar pago
    print(f"\n💰 El precio del {nombre_cafe} es: {precio_cafe}€")
    print("Introduce tus monedas:")
    total_introducido = 0.0
    total_introducido += obtener_moneda("🔸 Monedas de 10 cent: ") * valor_monedas["10cent"]
    total_introducido += obtener_moneda("🔸 Monedas de 20 cent: ") * valor_monedas["20cent"]
    total_introducido += obtener_moneda("🔸 Monedas de 50 cent: ") * valor_monedas["50cent"]
    total_introducido += obtener_moneda("🔸 Monedas de 1 euro: ") * valor_monedas["1euro"]
    total_introducido += obtener_moneda("🔸 Monedas de 2 euros: ") * valor_monedas["2euro"]

    if total_introducido < precio_cafe:
        print("❌ Dinero insuficiente. Dinero devuelto.")
        input("Presiona enter para continuar...")
        return False

    # Preparar café
    for ingrediente in ingredientes_cafe:
        recursos_disponibles[ingrediente] -= ingredientes_cafe[ingrediente]
    recursos_disponibles["dinero"] += precio_cafe

    cambio = round(total_introducido - precio_cafe, 2)
    print("\n✅ Preparando tu café...")
    if cambio > 0:
        print(f"💶 Tu cambio: {cambio}€")
    print(f"☕ ¡Aquí tienes tu {nombre_cafe}! ¡Disfrútalo!")
    print("══════════════════════════════════════")

    return True

# Bucle principal de la máquina
while maquina_encendida:
    limpiar_pantalla()
    print("══════════════════════════════════════")
    print("  🤖 Bienvenido a la máquina de café  ")
    print("══════════════════════════════════════")
    print("  1 - Ver recursos de la máquina")
    print("  2 - Pedir un café")
    print("  3 - Apagar la máquina")
    print("══════════════════════════════════════")

    opcion = input("Elige una opción (1/2/3): ")

    if opcion == "1":
        mostrar_recursos()

    elif opcion == "2":
        pedir = True
        while pedir:
            pedir = pedir_cafe()
            if not pedir:
                break
            continuar = input("¿Quieres otro café? (s/n): ")
            if continuar.lower() != "s":
                break
        apagar = input("¿Deseas apagar la máquina? (s/n): ")
        if apagar.lower() == "s":
            print("📴 Apagando la máquina... ¡Hasta luego!")
            maquina_encendida = False

    elif opcion == "3":
        print("📴 Apagando la máquina... ¡Hasta luego!")
        maquina_encendida = False

    else:
        print("❌ Opción no válida.")
        input("Presiona enter para continuar...")
