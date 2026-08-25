# se le pide al usaurio que ingrese un numero 
num = int(input("Ingrese un numero: "))
# se hace una condicional para saber si el numero es par o impar
if num % 2 == 0:
    print(num," es un numero par")
else:
    print(num," es un numero impar")