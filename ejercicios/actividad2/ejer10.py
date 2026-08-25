#imprimir los multiplos de 5 del 1 al 36
x = 36
y = 5
# se hace un ciclo while para recorrer los numeros del 1 al 36 y hacer la multiplicacion de los multiplos de 5
while y < x:
    #se hace una condicional para saber si el numero es multiplo de 5
    if y % 5 == 0:
        #se imprime el multiplo de 5
        print(y)
    #se incrementa el valor de y en 1
    y += 1