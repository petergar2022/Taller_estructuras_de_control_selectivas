def punto3 (A, B, C, D):
    condicion1 = False
    if(D == 0):
        condicion1 = True

    condicion2 = False
    if(D>0):
        condicion2 = True

    ac = A - C
    condicion3 = pow(ac, 2)

    ab = A - B
    condicion4 = pow(ab, 3) / D

    print(condicion1)
    print(condicion2)
    print(condicion3)
    print(condicion4)

punto3(1,2,3,4)