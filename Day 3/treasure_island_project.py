print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_ 
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_ 
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________/
*******************************************************************************
''')

print("Bienvenido a la Isla del Tesoro. \nTu misión es encontrar el tesoro.")
juega = input("¿Quieres jugar? S/N").upper()
if juega == "S":
    decision = input("Te encuentras enfrente de un desvío. \n¿A la izquierda o a la derecha? (L/R) ")
    if decision == "L":
        decision2 = input("Has llegado a un lago. \n¿Nadar o esperar? (N/E) ")
        if decision2 == "E":
            decision3 = input("Has llegado a una isla desierta. \n¿Abrir la caja roja, azul o amarilla? (R/A/B) ")
            if decision3 == "R":
                print("Has encontrado el tesoro. ¡Felicidades!")
            elif decision3 == "A":
                print("Has sido comido por una serpiente. \nGame Over.")
                exit()
            else:
                print("Se ha abierto el suelo y te has caido \nGame Over.")
                exit()
        else:
            print("Esperando te ha atacado un tucán. \nGame Over.")
            exit()
    else:
        print("Te has caído en un agujero. \nGame Over.")
        exit()

else:
    print("Pos na")
