#Entradas
nombre=input("Ingrese su nombre: ")
valor_r= float(input("Ingrese el monto de la compra: "))
#Caja Negra
mensaje=""
if(valor_r>0 and valor_r<50000):
    mensaje="Sr/Sra.",nombre,"su factura no presenta descuento, el valor a pagar es de:",valor_r
elif(valor_r>=50000 and valor_r<100000):
    descuento= valor_r*0.05
    valor_f= valor_r-descuento
    mensaje="Sr/Sra.",nombre,"su factura presenta un descuento del 5%, el valor a pagar es de:",valor_f
elif(valor_r>=100000 and valor_r<700000):
    descuento= valor_r*0.11
    valor_f= valor_r-descuento
    mensaje="Sr/Sra.",nombre,"su factura presenta un descuento del 5%, el valor a pagar es de:",valor_f
elif(valor_r>=700000 and valor_r<1500000):
    descuento= valor_r*0.18
    valor_f= valor_r-descuento
    mensaje="Sr/Sra.",nombre,"su factura presenta un descuento del 5%, el valor a pagar es de:",valor_f
else:
    descuento= valor_r*0.18
    valor_f= valor_r-descuento
    mensaje="Sr/Sra.",nombre,"su factura presenta un descuento del 5%, el valor a pagar es de:",valor_f
#Salidas
print(mensaje)
print("El valor de la compra fue de",valor_r,"y el descuento recibido fue de:",descuento)