# entrega-grupal

Enlaces de nuestros perfiles: @carmenm02(https://github.com/carmenm02) y @alexlomu(https://github.com/alexlomu)

Enlace de nuestro repositorio: https://github.com/carmenm02/entrega-grupal.git

EJERCICIO 1:

El ejercicio consiste en sumar los elementos de una matriz y obtener la suma de estos con numeros enteros.

El codigo que hemos usado es:

def simpleArraySum(): 
    
    filas_matriz = int(input("Introduce el numero de filas de tu matriz: "))
    
    columnas_matriz = int(input("Introduce el numero de columnas de tu matriz: "))
    
    tamano=filas_matriz*columnas_matriz
    
    matriz = list(map(int,input("Introduce los numeros separados por un espacio").split()))
    
    if len(matriz) != tamano:
        
        print("El numero de elementos no coincide con el tamaño de la matriz")
    
    else:
        
        suma = sum(matriz)
        
        print(suma)
    
simpleArraySum()

El figma que hemos usado es:




![figma_1](https://user-images.githubusercontent.com/91721507/146652932-5568350e-cc72-40f2-97c0-43711ccec032.JPG)




EJERCICIO 2:

El ejercicio consiste en que dos personas van a comparar sus calificaciones y se calculará quien de las dos ha obtenido la mayor calificación:

El codigo que hemos usado es:

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

El figma que hemos usado es:

<img width="884" alt="figma2" src="https://user-images.githubusercontent.com/91721886/146652307-befcf263-1310-43a9-9ccc-05af7f8b0f70.png">



EJERCICIO 3:

El ejercicio consiste en sumar los elementos de una matriz y obtener la suma de estos con numeros enteros teniendo en cuenta que pueden ser muy grandes.

El codigo que hemos usado es:

def aVeryBigSum(): 

    filas_matriz = int(input("Introduce el numero de filas de tu matriz: "))
    
    columnas_matriz = int(input("Introduce el numero de columnas de tu matriz: "))
    
    tamano=filas_matriz*columnas_matriz
    
    matriz = list(map(int,input("Introduce los numeros separados por un espacio").split()))
    
    if len(matriz) != tamano:
        
        print("El numero de elementos no coincide con el tamaño de la matriz")
    
    else:
        
        long = sum(matriz)
        
        print(long)
    
aVeryBigSum()

El figma que hemos usado es:


![figma_3](https://user-images.githubusercontent.com/91721507/146652936-43a886fe-b26a-4674-9c48-5a430ad10574.JPG)


EJERCICIO 4:

El programa crea una escalera compuesta por * de la cual podemos elegir su tamaño.

El codigo que hemos usado es:

def staircase():
    
    n = int(input("¿De que tamaño quieres la escalera?: "))
    
    for i in range(n+1):
        
        separacion = n - i
        
        print(" "*separacion +"# "*i)

staircase()

El figma que hemos usado es:

<img width="742" alt="figma 4" src="https://user-images.githubusercontent.com/91721886/146652484-3bae591d-4981-4987-bf96-3e56fdc871e1.png">

EJERCICIO 5:

El juego consiste en que dos jugadores van eliminando piedras de una cantidad inicial hasta que uno de ellos gana.

En cada movimiento un jugador puede eliminar solo 2,3 o 5 piedras, si no puede eliminarse esa cantidad pierde.

El codigo que hemos usado es:

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

El figma que hemos usado es:


![figma_5](https://user-images.githubusercontent.com/91721507/146652943-e9e89dbc-683d-4237-b104-fc4e5231be08.JPG)


EJERCICIO 6:

El ejercicio consiste en crear un laberinto y calcular la probabilidad de que la rana salga de el.

EL codigo que hemos usado es:

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
        
El figma que hemos usado es:

![figma_6](https://user-images.githubusercontent.com/91721507/146652946-a23c4efd-a2a5-4aa8-9de6-ae04652631b6.PNG)



EJERCICIO 7:

El ejercicio consiste en introducir una serie de calificaciones y segun si este valor esta comprendido entre ciertos valores los redondea o no.

El codigo que hemos usado es:

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

El figma que hemos usado es:

![figma_7](https://user-images.githubusercontent.com/91721507/146652948-41c7fceb-570f-48ca-a4ac-646360b1d280.PNG)


EJERCICIO 8:

El ejercicio consiste en introducir la posición de un manzano, un naranjo y una casa. Segun donde esten situados,el numero de naranjas y manzanas que caen y la distancia a la que estas caen nos indica cuales caen en la casa.

El codigo que hemos usado es:

def manzanas_naranjas():
    
    print("Introduce la posición inicial y la final de la casa separadas por un espacio.")
    
    s,t = map(int, input().strip().split(' '))
    
    print("Introduce la posición del manzano y del naranjo separadas por un espacio.")
    
    a,b = map(int, input().strip().split(' '))
    
    print("Introduce a la distancia a la que caen las manzanas del manzano y las naranjas del naranjo separadas por un espacio.")
    
    m,n = map(int, input().strip().split(' '))
    
    print("Introduce las distancias que hay entre cada par de manzanas separadas por un espacio.")
    
    apple = list(map(int, input().strip().split(' ')))
    
    print("Introduce las distancias que hay entre cada par de naranjas separadas por un espacio.")
    
    orange = list(map(int, input().strip().split(' ')))

    
    manzanas_caidas = sum([1 for f in apple if (f+a) >= s and (f+a) <= t])
    
    naranjas_caidas = sum([1 for f in orange if (f+b) >= s and (f+b) <= t])
    
    
    if manzanas_caidas != 1:
        
        print ("Han caído: "+ str(manzanas_caidas) + " manzanas en la casa")
    
    else:
        
        print ("Han caído: "+ str(manzanas_caidas) + " manzana en la casa")
    
    if naranjas_caidas != 1:   
      
        print ("Han caído: "+ str(naranjas_caidas) + " naranjas en la casa")
    
    else:
        
        print ("Han caído: "+ str(naranjas_caidas) + " naranjas en la casa")

EL figma que hemos usado es:

<img width="801" alt="figma 8" src="https://user-images.githubusercontent.com/91721886/146652909-fe6345e6-1f37-4f99-9eca-e41868abf451.png">


