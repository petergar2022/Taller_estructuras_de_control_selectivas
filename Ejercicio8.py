#Entradas
p= float(input("Ingrese el valor de P: "))
q= float(input("Ingrese el valor de Q: "))
#Caja Negra
formula= p**3+q**4-2*p**2
if(formula>680):
    print(p,"y",q,"satisfacen la expresión, el valor final es:",formula)
else:
    print(p,"y",q,"no Satisfacen la expresión")