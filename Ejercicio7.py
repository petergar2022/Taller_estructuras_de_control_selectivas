#Entradas
distancia=float(input("Ingrese los km recorridos:"))
#Caja Negra
mensaje=""
if(distancia<300):
    mensaje= "El valor del servicio es de: $50.000"
elif(distancia>=300 and distancia<=1000):
    distancia2= distancia-300
    cobro_q= distancia2*3000
    cobro_h=70000+cobro_q
    mensaje= "La distancia recorrida total fue de:",distancia,"kilometros con un total de:",cobro_h
else:
    distancia2=distancia-1000
    cobro_r=distancia2*9000
    cobro_h=150000+cobro_r
    mensaje= "La distancia recorrida total fue de:",distancia,"kilometros con un total de:",cobro_h
#Salida
print(mensaje)