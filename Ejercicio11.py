#Entrada
temperatura= float(input("Ingrese la temperatura actual: "))
#Caja Negra
deporte=""
if(temperatura>0 and temperatura <=10):
    deporte= "Marcha"
elif(temperatura>10 and temperatura <=32):
    deporte= "Esqui"
elif(temperatura>32 and temperatura <=70):
    deporte= "Golf"
elif(temperatura>70 and temperatura <=85):
    deporte= "Tenis"
elif(temperatura>85 and temperatura <=100):
    deporte= "Natacion"
#Salida
print("El deporte a practicar es:",deporte)