A= int(input("Ingrese el valor del numero A: "))
B= int(input("Ingrese el valor del numero B: "))
C= int(input("Ingrese el valor del numero C: "))
D= int(input("Ingrese el valor del numero D: "))

if(B >=5 and C>=5):
    A= A+1
    B=0
    C=0
    D=0
elif(B >=9 and C<5):
    B= B
    C=0
    D=0
elif(B <9 and C>=5):
    B= B+1
    C=0
    D=0
else:
    C=0
    D=0

print("El valor del numero es:",A,B,C,D)