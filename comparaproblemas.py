def compareTriplets():
    persona1 = input("Introduce el nombre de la primera persona: ")
    persona2 = input("Introduce el nombre de la segunda persona: ")
    calificaciones1 =[]
    calificaciones2 = []

    while True:
        nota1 = int(input("Introduzca la calificación de claridad del problema de "+ persona1 + ": "))
        calificaciones1.append(nota1)
        nota2 = int(input("Introduzca la calificación de originalidad de "+ persona1 + ": "))
        calificaciones1.append(nota2)
        nota3 = int(input("Introduzca la calificación de dificultad de"+ persona1 + ": "))
        calificaciones1.append(nota3)
        if nota1 <= 100 and nota1 >= 0 and nota2 <= 100 and nota2 >= 0 and nota3 <= 100 and nota3 >= 0:
            break
        else:
            print("Has introducido notas no válidas, por favor introduce las buenas.")
            calificaciones1 = []
    print("Las notas de", persona1, "son: ", calificaciones1)
    while True:
        nota4 = int(input("Introduzca la calificación de originalidad de "+ persona2 + ": "))
        calificaciones2.append(nota4)
        nota5 = int(input("Introduzca la calificación de originalidad de "+ persona2 + ": "))
        calificaciones2.append(nota5)
        nota6 = int(input("Introduzca la calificación de dificultad de"+ persona2 + ": "))
        calificaciones2.append(nota6)
        if nota4 <= 100 and nota4 >= 0 and nota5 <= 100 and nota5 >= 0 and nota6 <= 100 and nota6 >= 0:
            break
        else:
            print("Has introducido notas no válidas, por favor introduce las buenas.")
            calificaciones2 = []
    print("Las notas de", persona2, "son: ", calificaciones2)
    score1 = 0
    score2 = 0
    for i in range(len(calificaciones1)):
        if calificaciones1[i-1] > calificaciones2[i-1]:
            score1 += 1
        elif calificaciones1[i-1] < calificaciones2[i-1]:
            score2 += 1
    scoretotal = [score1,score2]
    print("La puntuacion total ha sido:", scoretotal)
    if score1 > score2:
        print(persona1 +"Ha obtenido una mayor puntuación")
    elif score1 < score2:
        print(persona2+"Ha obtenido una mayor puntuación.")
    else:
        print(persona1, "y", persona2, "han obtenido la misma puntuación.")
        


compareTriplets()