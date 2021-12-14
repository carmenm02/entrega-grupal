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