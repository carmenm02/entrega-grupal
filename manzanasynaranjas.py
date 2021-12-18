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
