from resources import recursos_disponibles, sabores_cafe, valor_monedas
from utils import limpiar_pantalla, obtener_moneda

class CoffeeMachine:
    def __init__(self):
        self.recursos = recursos_disponibles

    def mostrar_recursos(self):
        limpiar_pantalla()
        print("══════════════════════════════════════")
        print("     📊 Recursos actuales de la máquina")
        print("══════════════════════════════════════")
        for recurso, cantidad in self.recursos.items():
            print(f"🔹 {recurso.capitalize()}: {cantidad}")
        print("══════════════════════════════════════")
        input("Presiona enter para continuar...")

    def verificar_recursos(self, ingredientes):
        for ingrediente, cantidad in ingredientes.items():
            if cantidad > self.recursos.get(ingrediente, 0):
                print(f"🚫 No hay suficiente {ingrediente}.")
                input("Presiona enter para continuar...")
                return False
        return True

    def procesar_pago(self, precio):
        print(f"\n💰 El precio es: {precio}€")
        print("Introduce tus monedas:")
        total = 0.0
        total += obtener_moneda("🔸 Monedas de 10 cent: ") * valor_monedas["10cent"]
        total += obtener_moneda("🔸 Monedas de 20 cent: ") * valor_monedas["20cent"]
        total += obtener_moneda("🔸 Monedas de 50 cent: ") * valor_monedas["50cent"]
        total += obtener_moneda("🔸 Monedas de 1 euro: ") * valor_monedas["1euro"]
        total += obtener_moneda("🔸 Monedas de 2 euros: ") * valor_monedas["2euro"]

        if total < precio:
            print("❌ Dinero insuficiente. Dinero devuelto.")
            input("Presiona enter para continuar...")
            return False, 0.0

        cambio = round(total - precio, 2)
        self.recursos["dinero"] += precio
        return True, cambio

    def preparar_cafe(self, nombre_cafe):
        limpiar_pantalla()
        ingredientes = sabores_cafe[nombre_cafe]["ingredientes"]
        precio = sabores_cafe[nombre_cafe]["precio"]

        if not self.verificar_recursos(ingredientes):
            return

        pagado, cambio = self.procesar_pago(precio)
        if not pagado:
            return

        for ingrediente, cantidad in ingredientes.items():
            self.recursos[ingrediente] -= cantidad

        print("\n✅ Preparando tu café...")
        if cambio > 0:
            print(f"💶 Tu cambio: {cambio}€")
        print(f"☕ ¡Aquí tienes tu {nombre_cafe}! ¡Disfrútalo!")
        print("══════════════════════════════════════")
        input("Presiona enter para continuar...")
