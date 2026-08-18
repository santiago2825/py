#imprimir la suma de los numeros pares del 1 al 60
sum = 0
# se hace un ciclo for para recorrer los numeros del 1 al 60 y hacer la suma de los pares
for i in range(1, 61):
    #se hace una condicional para saber si el numero es par
    if i % 2 == 0:
        #se hace la suma de los numeros pares
        sum += i
        #se imprime la suma de los numeros pares
print("La suma de los numeros pares del 1 al 60 es: ", sum)