notas = {"ana":8,"luis":5,"marta":9,"pedro":6,"sofia":4}
suma = 0
for i in notas.values():
    suma+=i
    resultado = suma/len(notas)

print(resultado)