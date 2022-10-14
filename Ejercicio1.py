def intereses(tasa, cantidad):
    cantidadFinal = cantidad * tasa
    loEsperado = 100000
    mensaje = ''
    if(cantidadFinal < loEsperado):
        mensaje = 'Esta tasa no sirve'
    else:
        mensaje = f"Esta tasa si sirve y el valor final es {cantidadFinal}"

    return mensaje

tasa = int(input('Cual es la tasa de interes? '))
cantidad = int(input('Cuanto dinero hay al principio? '))

intereses(tasa, cantidad)