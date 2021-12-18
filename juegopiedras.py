import random
opciones = [2, 3, 5]
def gameOfStones():
    global numeroPiedras
    numeroPiedras = int(input("¿Con cuantas piedras quieres jugar?: "))
    turno = 1
    while True:
        while numeroPiedras != 0 and numeroPiedras != 1:
            if turno == 1:
                print("Es el turno del jugador 1")
                print("Hay", numeroPiedras," piedras en el tablero")
                if numeroPiedras == 2:
                    eliminar = 2
                elif numeroPiedras == 3:
                    eliminar = 3
                elif numeroPiedras == 4:
                    eliminar = 3
                elif numeroPiedras == 5:
                    eliminar = 5
                elif numeroPiedras == 6:
                    eliminar = 5
                elif numeroPiedras >= 7 and numeroPiedras < 9:
                    eliminar = random.choice(opciones)
                elif numeroPiedras == 9:
                    eliminar = 2
                elif numeroPiedras == 10:
                    eliminar = 3
                elif numeroPiedras == 11:
                    eliminar = random.choice(opciones)
                elif numeroPiedras == 12:
                    eliminar = 5
                elif numeroPiedras >= 13:
                    eliminar = random.choice(opciones)
                numeroPiedras = numeroPiedras - eliminar
                print("El jugador 1 ha eliminado", eliminar, "piedras")
                turno += 1
            elif turno == 2:
                print("Es el turno del jugador 2")
                print("Hay", numeroPiedras," piedras en el tablero")
                if numeroPiedras == 2:
                    eliminar = 2
                elif numeroPiedras == 3:
                    eliminar = 3
                elif numeroPiedras == 4:
                    eliminar = 3
                elif numeroPiedras == 5:
                    eliminar = 5
                elif numeroPiedras == 6:
                    eliminar = 5
                elif numeroPiedras >= 7 and numeroPiedras < 9:
                    eliminar = random.choice(opciones)
                elif numeroPiedras == 9:
                    eliminar = 2
                elif numeroPiedras == 10:
                    eliminar = 3
                elif numeroPiedras == 11:
                    eliminar = random.choice(opciones)
                elif numeroPiedras == 12:
                    eliminar = 5
                elif numeroPiedras >= 13:
                    eliminar = random.choice(opciones)
                numeroPiedras = numeroPiedras - eliminar
                print("El jugador 2 ha eliminado", eliminar, "piedras")
                turno -= 1
        ganador = "P" + str(turno)
        break
    print("Hay", numeroPiedras," piedras en el tablero")
    print("Ha ganado", ganador)




gameOfStones()