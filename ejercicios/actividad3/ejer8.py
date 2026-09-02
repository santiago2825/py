medidas = [1.50,1.76,1.66,1.74,1,40,1.60,1.80,1.59]

suma = 0
altos = 0
bajos = 0

for i in medidas:
    suma += i
    media = suma / len(medidas)

for i in medidas:
    if i > media:
        altos += 1
    else:
        bajos += 1
print("medidad mayor que la media son:",altos)
print("medida menor que la media son:",bajos)
