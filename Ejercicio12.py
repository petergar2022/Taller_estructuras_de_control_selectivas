valores = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50]

def punto12(cantidad):
    respuesta = ''
    while(cantidad >= 50):
        for i in valores:
            if (i <= cantidad):
                respuesta += f'{i}, '
                cantidad -= i
                break   
    
    l = len(respuesta)
    return respuesta[:l-2]

print(punto12(2251))