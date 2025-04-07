print("""--Bienvenido a la pizzería de Python--
      Aquí puedes personalizar tu pizza a tu gusto. Los precios son los siguientes:
      - Pequeña (S) = 15.00
      - Mediana (M) = 20.00
      - Grande (L) = 25.00
      - Peppero ni en pizza pequeña = +2.00
      - Pepperoni en pizza mediana y grande = +3.00
      - Extra de queso en cualquier pizza = +1.00\n""")

tamaño = input("¿De que tamaño quieres la pizza? (S, M, L): ").upper()
#Comprobar si el tamaño es correcto
while tamaño not in ["S", "M", "L"]:
    tamaño = input("Tamaño no válido. Por favor, elige S, M o L. ").upper()

pepperoni = input("¿Quieres pepperoni? (S/N): ").upper()
while pepperoni not in ["S", "N"]:
    pepperoni = input("¿Que pesadito no? Que me digas si quieres pepperoni cojone (S/N): ").upper()

extra_queso = input("¿Quieres extra queso? (S/N): ").upper()
while extra_queso not in ["S", "N"]:
    extra_queso = input("¿Quieres extra de queso o no pichita? no marees (S/N): ").upper()

#Calcular el precio de la pizza
precio_total = 0
if tamaño == "S":
    precio_total += 15.00
    if pepperoni == "S":
        precio_total += 2.00
elif tamaño == "M":
    precio_total += 20.00
    if pepperoni == "S":
        precio_total += 3.00
elif tamaño == "L":
    precio_total += 25.00
    if pepperoni == "S":
        precio_total += 3.00

if extra_queso == "S":
    precio_total += 1.00

print(f'El precio de su pizza es: {precio_total}, pagame y no vuelvas a volver a comer pizza aquí en tu vida.')
#Fin del programa
