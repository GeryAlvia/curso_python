#20. A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados números entre 0 y 10

var1=int(input("Introduzca un valor entre el 0 y el 10"))
var2=int(input("Introduzca un valor entre el 0 y el 10"))

if var1<var2: var1>var2 and var1>0 and var1<10 and var2>0 and var2<10: print("El número",var2,"es mayor que",var1,".")      
elif var1>var2 and var1>0 and var1<10 and var2>0 and var2<10:
    print("El número",var1,"es mayor que",var2,".")
elif  var1>var2 and var1==0 and var1<10 and var2>0 and var2<10:
    print("El número",var1,"es mayor que",var2,".")          

else:
    print("Uno o los dos números están fuera de los límites establecidos")
    input()
