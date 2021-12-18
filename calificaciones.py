def nuevas_notas():
    calificaciones = list(map(int,input("Introduce las calificaciones separadas por un espacio: ").split()))
    notas_finales = []
    for i in range(len(calificaciones)):
        if calificaciones[i] >= 0 and calificaciones[i] <= 100:
            if calificaciones[i] >= 40:
                if calificaciones[i]%5 == 3: 
                    calificaciones[i] += 2
                elif calificaciones[i]%5 ==4:
                    calificaciones[i] += 1
                notas_finales.append(calificaciones[i])
            else:
                notas_finales.append(calificaciones[i])
            
        else:
            print("Has introducido notas incorrectas")
    print("Las notas finales son: "+ str(notas_finales))
nuevas_notas()