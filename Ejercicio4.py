#Entrada
inversion= float(input("Ingrese el valor de la inversion a realizar: "))
#Caja Negra
if(inversion>5000000):
    contado= inversion*0.55
    prestamo_banco= inversion*0.30
    interes_banco1= float(input("Ingrese el porcentaje del valor de los intereses del banco: "))
    interes_banco2= (prestamo_banco*interes_banco1)/100
    credito1= inversion*0.15
    creditoj= credito1*0.2
    pagop= contado+prestamo_banco+interes_banco2+credito1+creditoj
    print("El valor final a pagar es de:",pagop)
else:
    contado= inversion*0.7
    credito1= inversion*0.3
    creditoj= credito1*0.2
    pagop= contado+credito1+creditoj
    print("El valor final a pagar es de:",pagop)