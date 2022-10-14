def montoAPagar (lecturaAnterior, lecturaActual):
    diferencia = abs(lecturaActual - lecturaAnterior)
    monto = 0

    if(diferencia < 100):
        monto = diferencia * 4600
    elif(diferencia > 100 and diferencia < 300):
        monto = diferencia * 80000
    elif(diferencia > 300 and diferencia < 500):
        monto = diferencia * 100000
    else:
        monto = diferencia * 120000

    return monto


print(montoAPagar(1000, 1300))