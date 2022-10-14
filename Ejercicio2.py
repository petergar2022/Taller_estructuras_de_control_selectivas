def nuevoSueldo(sueldoActual):
    nuevoSueldo = 0
    if(sueldoActual < 900000):
        nuevoSueldo = sueldoActual * 1.12
    else:
        nuevoSueldo = sueldoActual * 1.15
    return nuevoSueldo

sueldoActual = int(input('Cual es el sueldo actual? '))
print(nuevoSueldo(sueldoActual))