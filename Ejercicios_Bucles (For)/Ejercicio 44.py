#44. Realiza un programa que recorra todos los números comprendidos de 0 a 100 realizando saltos de 3 en 3. El resultado debe aparecer por pantalla en una línea con los números separados por.

i=0
multi=0
n=int(input("Introduce un número por teclado"))
while i<=10:
    multi=i * n
    print(multi)
    i+=1
    print(n,end=' ')