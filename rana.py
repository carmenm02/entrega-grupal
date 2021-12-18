mapa= [
    ["X" , "I" , "X" , "X" , "X" , "X" , "X"],
    ["X" , " " , "X" , "X" , "T1" , " " , "X"],
    ["X" , " " , "T2" , "X" , " " , " " , "X"],
    ["X" , " " , " " , "X" , "B" , " " , "X"],
    ["X" , " " , " " , "X" , "T2" , " " , "X"],
    ["X" , "T1" , "B" , "X" , "X" , " " , "X"],
    ["X" , "X" , "X" , "X" , "X" , "S" , "X"],
]

x = 1
y = 1

print("La rana empieza en la posición (0,0)")
print((mapa[y])[x])
i = 0

while (mapa[y])[x] != "X":
    direccion = input("Selecciona la dirección en la que deseas moverte (ARRIBA, ABAJO, DERECHA, IZQUIERDA): ")
    
    if direccion == "ABAJO" or "ARRIBA" or "DERECHA" or "IZQUIERDA":
        print("Has seleccionado {}".format(direccion))
    
    if direccion == "ABAJO":
        x = x
        y = y + 1      
    elif direccion == "ARRIBA":
        x = x
        y = y - 1

    elif direccion == "DERECHA":
        x = x - 1
        y = y 

    elif direccion == "IZQUIERDA":
        x = x + 1
        y = y 


    else:
        print("SOLO SE PUEDEN ELEGIR LAS OPCIONES DE DIRECCIÓN EXPLICADAS, ELIGE BIEN")
        print("\n")

    print("Estás en la casilla ({},{})".format(x,y))
    if (mapa[y])[x] == ' ':
        print("La casilla elegida NO es un muro, puede continuar en el laberinto")
    elif (mapa[y])[x] == 'S':
        print("Has llegado a la salida del laberibnto. ¡HAS GANADO!")
        break
    elif (mapa[y])[x] =="T1":
        if(x==1  and y==5 ):
            x = 4
            y = 1
            print("Has encontrado un tunel, la rana se mueve a la casilla (4,3)")
        if(x==4 and y==1):
            x = 1
            y = 5
            print("Has encontrado un tunel, la rana se mueve a la casilla (1,4)")
        elif (mapa[y])[x] == "T2":
           if(x==2  and y==2 ):
            x = 4
            y = 4
            print("Has encontrado un tunel, la rana se mueve a la casilla (5,2)")
        if(x==4 and y==4):
            x = 2
            y = 2
            print("Has encontrado un tunel, la rana se mueve a la casilla (5,4)") 
    else:
        print("La casilla es un muro \nReinicia el programa para seguir jugando")