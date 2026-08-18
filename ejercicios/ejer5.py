# se le pide al usuario que ingrese un angulo
angulo = float(input("Ingrese un angulo: "))
# se hace una condicional para saber si el angulo es agudo, recto u obtuso
if angulo < 90:
    print("El angulo es agudo")
elif angulo == 90:
    print("El angulo es recto")
else:
    print("El angulo es obtuso")