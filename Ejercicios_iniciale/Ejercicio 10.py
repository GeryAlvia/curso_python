#10.Introduce por teclado dos números y muestre por pantalla la siguiente información:cociente, resto y si el dividendo es par o impar.

Var1=float(input("Introduce un número: "))
Var2=float(input("Introduce un número: "))
coeficiente=Var1//Var2
resto=Var1%Var2
par=Var2%2
impar=Var1%1


print("El coeficiente es:",coeficiente)
print("El resto es:",resto)
if par==0:
    print("El dividiendo es par")
elif impar==0:
    print("El dividiendo es impar")
else:
    print("El dividiendo es:")    

      
