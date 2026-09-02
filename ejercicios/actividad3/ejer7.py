temperatura = [22.0,18.5,15.7,25.7,20,0,22.0]

suma = 0

for i in temperatura:
    suma += i
    media = suma /len(temperatura)

contador = 0
for i in temperatura:
    if i >= media:
        contador += 1
print("la media de las temperaturas es :",media)
print("temperaturas mayor o igual que la media son:",contador)