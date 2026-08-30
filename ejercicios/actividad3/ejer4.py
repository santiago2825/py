lista = [-12,45,23,-23,45,-26,98,0,23,0,0,23,-12,32,0]

negativo = 0
positivo = 0
neutro = 0

for i in lista:
    if i > 0:
        positivo += 1
    elif i < 0:
        negativo += 1
    else:
        neutro += 1
print("los numeros positivos en total son :",positivo)
print("los numeros negativo en total son :",negativo)
print("los numeros neutro en total son :",neutro)