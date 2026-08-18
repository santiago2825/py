#imprimir los cubos de los numeros pares del 2 al 20
for i in range(2,21):
    # se hace una condicional para saber si el numero es par
    if i % 2 == 0:
        #se imprime el cubo de cada numero par
        print(i**3)