gavel_ascii = '''
                    

                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\
'''

print(gavel_ascii)
print("Bienvenido a la subasta secreta")

concursantes = {}
while True:
    nombre = input("¿Cuál es tu nombre? ")
    oferta = int(input("¿Cuál es tu oferta? $"))
    concursantes[nombre] = oferta
    continuar = input("¿Hay otro concursante? (si/no): ").lower()
    if continuar != "si":
        break

#Obtener el concursante con la oferta más alta
ganardor = ""
ganancia_maxima = 0
for concursante in concursantes:
    oferta = concursantes[concursante]
    if oferta > ganancia_maxima:
        ganancia_maxima = oferta
        ganardor = concursante
print(f"El ganador es {ganardor} con una oferta de ${ganancia_maxima}.")