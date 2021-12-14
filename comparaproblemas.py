def compareTriplets():
    persona1 = input("Introduce el nombre de la primera persona: ")
    persona2 = input("Introduce el nombre de la segunda persona: ")
    calificaciones1 =[]
    calificaciones2 = []

    
    nota1 = int(input("Introduzca las calificaciones de uno en uno  de la persona1"))
    calificaciones1.append(nota1)
    nota2 = int(input("Introduzca las calificaciones de uno en uno  de la persona1"))
    calificaciones1.append(nota2)
    nota3 = int(input("Introduzca las calificaciones de uno en uno  de la persona1"))
    calificaciones1.append(nota3)
    print(calificaciones1)

    nota4 = int(input("Introduzca las calificaciones de uno en uno  de la persona2"))
    calificaciones2.append(nota4)
    nota5 = int(input("Introduzca las calificaciones de uno en uno  de la persona2"))
    calificaciones2.append(nota5)
    nota6 = int(input("Introduzca las calificaciones de uno en uno  de la persona2"))
    calificaciones2.append(nota6)
    print(calificaciones2)
    score1 = 0
    score2 = 0
    for i in range(len(calificaciones1)):
        if calificaciones1[i-1] > calificaciones2[i-1]:
            score1 += 1
        elif calificaciones1[i-1] < calificaciones2[i-1]:
            score2 += 1
    scoretotal = [score1,score2]
    print(scoretotal)


compareTriplets()