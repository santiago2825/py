lista = [12,45,23,23,23,45,26,98]
suma_pares = 0
suma_impares = 0
for i in lista:
    if i %2 ==0:
        suma_pares += i
    else:
        suma_impares += i

print("la suma de los numeros pares es ",suma_pares)
print("la suma de los numeros imapres es ",suma_impares)