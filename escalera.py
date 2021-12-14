def staircase():
    n = int(input("¿De que tamaño quieres la escalera?: "))
    for i in range(n+1):
        separacion = n - i
        print(" "*separacion +"# "*i)
staircase()