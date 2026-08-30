arreglo = [12,45,34,54,33]
buscar = 34

if buscar in arreglo:
    posicion = arreglo.index(buscar)
    print(buscar,"esta en la posicion",posicion)
else:
    print(buscar,"no esta en el arreglo")