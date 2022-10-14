from math import sqrt

def punto16(a, b, c):
    x1 = 0
    x2 = 0
    d = pow(b, 2)-(4*a*c)
    if(d == 0):
        x1 = -b/(2*a)
        x2 = x1
    elif (d > 0):
        x1 = (-b + sqrt(d))/(2*a)   
        x2 = (-b - sqrt(d))/(2*a) 
    else:
        return 'Ecuacion no tiene solucion en numeros reales'
    
    return f'X1 = {x1}, X2 = {x2}'

print(punto16(6, 11, -35))