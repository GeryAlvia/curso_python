#Ejercicio 4 
SP95= 1.765
SP98=1.913
GA=1.746
GAA=1.839
print("****GASOLINERA****")
print("1. Sin plomo 95")
print("3. Sin plomo 98")
print("3. Gasóleo A")
print("4. Gasóleo A+")
print("***************")
gasolina=int(input("Escoja el tipo de combustible: "))
if gasolina==1:
             lit=float(input("Introduzca el número de litros a repostar"))
             precio=lit*SP95
             print("El precio a pagar es: ",precio)
elif gasolina==2:
             lit=float(input("Introduzca el número de litros a repostar"))
             precio=lit*SP98
             precio2=precio/100*90
             print("El precio a pagar es: ",precio,"y con el descuento queda en: ",precio2)
elif gasolina==3:
             lit=float(input("Introduzca el número de litros a repostar"))
             precio=lit*GA
             print("El precio a pagar es: ",precio)
elif gasolina==4:
             lit=float(input("Introduzca el número de litros a repostar"))
             precio=lit*GAA
             precio2=round(precio/100*90, 2)
             print("El precio a pagar es: ",precio,"y con el descuento queda en: ",precio2)
else:
        print("El valor introducido no esta dentro del menú de la selección")
             
             
      
