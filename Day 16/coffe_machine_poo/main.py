from coffee_machine import CoffeeMachine
from utils import limpiar_pantalla

def menu_principal():
    cafetera = CoffeeMachine()
    maquina_encendida = True

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
            cafetera.mostrar_recursos()

        elif opcion == "2":
            while True:
                limpiar_pantalla()
                print("☕ ¿Qué tipo de café deseas?")
                print("  1 - Espresso")
                print("  2 - Late")
                print("  3 - Cappuccino")
                print("══════════════════════════════════════")
                tipo = input("Elige una opción (1/2/3): ")
                tipos = {"1": "Espresso", "2": "Late", "3": "Cappuccino"}

                if tipo not in tipos:
                    print("❌ Opción no válida.")
                    input("Presiona enter para continuar...")
                    continue

                cafetera.preparar_cafe(tipos[tipo])
                otro = input("¿Quieres otro café? (s/n): ").lower()
                if otro != "s":
                    break

            apagar = input("¿Deseas apagar la máquina? (s/n): ").lower()
            if apagar == "s":
                print("📴 Apagando la máquina... ¡Hasta luego!")
                maquina_encendida = False

        elif opcion == "3":
            print("📴 Apagando la máquina... ¡Hasta luego!")
            maquina_encendida = False

        else:
            print("❌ Opción no válida.")
            input("Presiona enter para continuar...")

if __name__ == "__main__":
    menu_principal()
