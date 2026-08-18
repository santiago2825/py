#se le coloca valor a las variables
x = 5
y = 10
z = 15
# se hace una variable para comparar cual es el mayor de las tres variables
if x > y and x > z:
    print(x," es mayor que ",y," y ",z)
elif y > x and y > z:
    print(y," es mayor que ",x," y ",z)
else:
    print(z," es mayor que ",x," y ",y)